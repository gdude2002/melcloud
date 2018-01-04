# code=utf-8
# File adapted from the pypa sample project at https://github.com/pypa/sampleproject

"""
A module providing access to Mitsubishi's MELCloud API

Many thanks to the following people for their work on reverse-engineering this API!
* https://github.com/ilcato/homebridge-melcloud/
* http://mgeek.fr/blog/un-peu-de-reverse-engineering-sur-melcloud
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import sys

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='melcloud',
    version='0.0.3',
    description='MELCloud API library',
    long_description=long_description,
    url='https://github.com/gdude2002/melcloud',
    author='Gareth Coles',
    author_email='gdude2002@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking :: Monitoring',

        'Framework :: AsyncIO',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='melcloud mitsubishi ecodan http web heating iot',
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=['contrib', 'docs', 'tests', 'old']),
    install_requires=['requests', 'aiohttp', 'inflection', "dataclasses", "arrow"],
)
