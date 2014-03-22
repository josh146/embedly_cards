#!/usr/bin/env python2.7

from setuptools import setup

version = __import__('embedly_cards').__version__
download_url = 'https://github.com/josh146/embedly_cards/archive/{}.zip'.format(version)

info={
    'name'            : 'embedly_cards',
    'version'         : version,
    'author'          : 'Josh Izaac',
    'author_email'    : 'josh@iza.ac',
    'url'             : 'https://github.com/josh146/embedly_cards',
    'download_url'    : download_url,
    'license'         : 'GPLv3',
    'description'     : 'Pelican plugin for embedding external content using Embed.ly Cards',
    'long_description': open('README.rst').read(),
    'provides'        : ["embedly_cards"],
    'install_requires': ['docutils', 'pelican'],
    'packages'        : ['embedly_cards']
  }

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Text Processing",
  ]


setup(classifiers=classifiers, **(info))
