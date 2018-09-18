#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

__author__ = "drewpearce <drew@caffdev.com>"
__copyright__ = "Copyright 2018, Drew Pearce"

description = 'Lego for getting a random "fact" from the Portal 2 Fact Sphere'
name = 'legos.fact_sphere'
setup(
    name=name,
    version='0.1.0',
    namespace_package=name.split('.')[:-1],
    license='GPL3',
    description=description,
    author='drewpearce',
    url='https://github.com/Legobot/' + name,
    install_requires=[
        'legobot',
        'pyyaml'
    ],
    classifiers=[
        'License :: OSI Approved :: GPL 3',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha'
    ],
    packages=find_packages()
)
