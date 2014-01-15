import os

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    author = 'Reece Hart',
    author_email = 'reecehart+rcore@gmail.com',
    description = "Reece's commonly used utilities",
    license = 'MIT',
    long_description = open('README.rst','r').read(),
    name = "rcore",
    packages = ['rcore'],
    url = 'https://bitbucket.org/reece/rcore',
    use_hg_version = True,
    zip_safe = True,

    classifiers = [
        "License :: OSI Approved :: MIT License",
        ],

    keywords = [
        ],

    install_requires = [
        # rcore needs only Python >=2.7
        ],

    setup_requires = [
        'hgtools',
        'nose',
        ],    

    tests_require = [
        'nose',
    ]
)
