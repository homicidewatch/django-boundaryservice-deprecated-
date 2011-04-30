#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "django-boundaryservice",
    description = "A reusible boundaries API for GeoDjango",
    long_description = open('README.md').read(),
    version = "0.1.0",
    packages = [
        'boundaryservice',
        'boundaryservice.migrations',
        'boundaryservice.management',
        'boundaryservice.management.commands'
    ],
    license = "MIT",
)