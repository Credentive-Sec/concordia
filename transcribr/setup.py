#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = __import__('transcribr').get_version()
INSTALL_REQUIREMENTS = [
    'Django<2.1',
    'djangorestframework',
    'coreapi'
]
DESCRIPTION = 'Transcription and tagging for crowdsourcing'
CLASSIFIERS = '''\
Environment :: Web Environment
Framework :: Django :: 2.0
Development Status :: 2 - Pre-Alpha
Programming Language :: Python
Programming Language :: Python :: 3.6
'''.splitlines()

with open('README.rst', 'r') as f:
    LONG_DESCRIPTION = f.read()


setup(
    name='transcribr',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIREMENTS,
    classifiers=CLASSIFIERS,
)
