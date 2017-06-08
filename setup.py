#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/8 上午11:27
# @Author  : 袁平华
# @Site    : 
# @File    : setup.py
# @Software: PyCharm Community Edition



import os
from setuptools import setup, find_packages


def fread(fname):
    filepath = os.path.join (os.path.dirname (__file__), fname)
    with open (filepath, 'r') as fp:
        return fp.read ( )


setup (
    name='cocoa_packer',
    version='1.3',
    description='A cocoapods package packer',
    keywords='cocoapods  package',
    url='https://github.com/zhipengbird/cocoapodsPackage',
    author='yuanpinghua',
    author_email='yuanpinghua@yeah.net',
    license='MIT',
    packages=find_packages ( ),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'cocoa_packer = package.cocoa_package:main'
        ]
    },
    # long_description=fread("README.md")
    # install_requires =['shutil'],
)