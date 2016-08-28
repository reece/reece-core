import pkg_resources
__version__ = pkg_resources.get_distribution(__package__ or pkg_resources.Distribution(version='')).version
