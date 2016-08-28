import os

from setuptools import setup, find_packages

def version_handler(mgr, options):
    version = mgr.get_current_version()
    if version.endswith('dev'):
        version += '-' + mgr._invoke('log','-l1','-r.','--template','{node|short}').strip()
    return version

setup(
    #use_hg_version = True,
    author = 'Reece Hart',
    author_email = 'reecehart+reece@gmail.com',
    description = "Reece's commonly used utilities",
    license = 'MIT',
    long_description = open('README.rst','r').read(),
    name = "reece",
    packages = ['reece'],
    test_suite = 'nose.collector',
    url = 'https://bitbucket.org/reece/reece',
    use_vcs_version = {'version_handler': version_handler},
    zip_safe = True,

    classifiers = [
        "License :: OSI Approved :: MIT License",
        ],

    keywords = [
        ],

    install_requires = [
        ],

    setup_requires = [
        'hgtools',
        'nose',
        ],    

    tests_require = [
        'nose',
    ]
)
