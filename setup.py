#!/usr/bin/env python

import os
from phockup import version
from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fn:
        return fn.read()


setup(
    name='phockup',
    version=version,
    author='Ivan Dokov',
    author_email='ivan.dokov@gmail.com',
    description='Media sorting tool to organize photos and videos from your camera in folders by year, month and day.',
    long_description=read('readme.md'),
    entry_points={
        'console_scripts': [
            'phockup=phockup:main',
        ],
    },
    # install_requires=read('requirements.txt'),
    packages=find_packages()
)