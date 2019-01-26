#!/usr/bin/env python3
# pylint: disable=missing-docstring
import os
from setuptools import find_packages, setup


def read(fname):
    """
    Utility function to read the large files like the README file.

    Used for the long_description.  It's nice, because now:
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw
    string in below ...
    """
    with open(os.path.join(os.path.dirname(__file__), fname)) as filepointer:
        return filepointer.read()


setup(
    name="autovenv",
    version="0.6",
    author="Michael Trunner",
    author_email="michael@trunner.de",
    maintainer="Michael Trunner",
    maintainer_email="michael@trunner.de",
    description=("Helper script for venv and pip"),
    license="Apache License 2.0",
    keywords="pip venv requirements virtualenv",
    url="https://github.com/trunneml/autovenv",
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    py_modules=['autovenv'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta"
        #"Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License 2.0",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Archiving :: Packaging"
    ],
    # We only depend on venv but this is a standard python 3 lib
    install_requires=[],
    zip_safe=True,
)
