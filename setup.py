import os

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

def version_handler(mgr, options):
    import IPython; IPython.embed()
    version = mgr.get_current_version()
    if version.endswith('dev'):
        version += '-' + mgr._invoke('log','-l1','-r.','--template','{node|short}').strip()
    return version

setup(
    #use_hg_version = True,
    author = 'Reece Hart',
    author_email = 'reecehart+rcore@gmail.com',
    description = "Reece's commonly used utilities",
    license = 'MIT',
    long_description = open('README.rst','r').read(),
    name = "rcore",
    packages = ['rcore'],
    test_suite = 'nose.collector',
    url = 'https://bitbucket.org/reece/rcore',
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
