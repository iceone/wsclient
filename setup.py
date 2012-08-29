#!/usr/bin/env python

try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.core import setup, Extension, Command

setup(
    name='wsclient',
    version='0.1.0',
    description='Websocket client using Tornado IOLoop.',
    long_description=open('README.rst').read(),
    author='Jeff Balogh',
    author_email='github@jeffbalogh.org',
    url='http://jbalogh.me',
    packages=['wsclient'],
    license='MIT',
    install_requires=[
        'tornado'
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ]
)
