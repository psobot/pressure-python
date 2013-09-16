from distutils.core import setup

setup(
    name="pressure",
    description="Client library for interfacing with Pressure queues.",
    version=str(__import__("pressure").__version__),
    author="Peter Sobot",
    author_email="contact@petersobot.com",
    url="https://github.com/psobot/pressure-python",
    download_url="https://github.com/psobot/pressure-python/tarball/master",
    package_dir={'pressure': 'pressure'},
    packages=['pressure'],
    install_requires=['redis>=2.7.2'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
    ],
)
