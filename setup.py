#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='homoglyphs',
    version='1.2.2',

    author='orsinium',
    author_email='master_fess@mail.ru',

    description='Get homoglyphs for text, convert text to ASCII.',
    long_description=open('README.rst').read(),
    keywords='homoglyphs ascii utf8 text homoglyph similar letters',

    packages=['homoglyphs'],
    package_data={'': ['*.json']},
    requires=['python (>= 2.7)'],

    url='https://github.com/orsinium/homoglyphs',
    download_url='https://github.com/orsinium/homoglyphs/tarball/master',

    license='GNU Lesser General Public License v3.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    ],
)
