#!/usr/bin/env python

import os
import sys
import logging
import pressure
import argparse

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler(sys.stderr))
log.setLevel(logging.INFO)


def produce(host, port, queue):
    log.info(
        "Passing lines from stdin to queue '%s' on %s:%d.",
        queue, host, port
    )
    q = pressure.PressureQueue(queue, 5, host=host, port=port)
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        q.put(line)


def consume(host, port, queue):
    log.info(
        "Passing lines from queue '%s' on %s:%d to stdout.",
        queue, host, port
    )
    q = pressure.PressureQueue(queue, 5, host=host, port=port)
    for line in q:
        sys.stdout.write(line)
        sys.stdout.flush()


def run():
    parser = argparse.ArgumentParser(
        description='Bridge between a `pressure` queue and a unix pipe.'
    )
    parser.add_argument('--host', type=str,
                        help='the redis host to connect to',
                        default='127.0.0.1')
    parser.add_argument('--port', type=int,
                        help='the redis port to connect to',
                        default='6379')
    parser.add_argument('--queue', type=str,
                        help='the name of the queue to connect to',
                        default=str(os.getpid()))
    parser.add_argument('--produce', action='store_true',
                        help='make this bridge read from stdin and '
                             'push each line to the queue',
                        default=False)
    parser.add_argument('--consume', action='store_true',
                        help='make this bridge read from the queue and '
                             'write each line to stdout',
                        default=False)
    args = parser.parse_args()

    if args.consume and args.produce:
        raise ValueError(
            "Cannot produce and consume at the same time. "
            "Please pass --produce or --consume."
        )
    elif args.consume:
        consume(args.host, args.port, args.queue)
    elif args.produce:
        produce(args.host, args.port, args.queue)
    else:
        raise ValueError(
            "Please pass --produce or --consume."
        )

if __name__ == "__main__":
    run()
