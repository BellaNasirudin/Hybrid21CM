#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import os
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import relpath
from os.path import splitext
from os.path import expanduser

from setuptools import Extension
from setuptools import find_packages
from setuptools import setup
from distutils.core import Extension as DExtension

from shutil import copyfile, move
from distutils.dir_util import copy_tree


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

# Enable code coverage for C code: we can't use CFLAGS=-coverage in tox.ini, since that may mess with compiling
# dependencies (e.g. numpy). Therefore we set SETUPPY_CFLAGS=-coverage in tox.ini and copy it to CFLAGS here (after
# deps have been safely installed).
if 'TOXENV' in os.environ and 'SETUPPY_CFLAGS' in os.environ:
    os.environ['CFLAGS'] = os.environ['SETUPPY_CFLAGS']

setup(
    name='py21cmmc',
    version=find_version("src", "py21cmmc", "__init__.py"),
    license='MIT license',
    description='An extensible MCMC framework for 21cmFAST',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Brad Greig',
    author_email='greigb@unimelb.edu.au',
    url='https://github.com/BradGreig/21CMMC',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords=[
        "Epoch of Reionization", "Cosmology"
    ],
    install_requires=[
        'click',
        #'tqdm',
        'numpy',
        'pyyaml',
        #'cosmoHammer',
        'cffi>=1.0',
        'scipy',
        'astropy>=2.0',
        #'powerbox>=0.5.4',
        #'h5py'
    ],
    entry_points={
        'console_scripts': [
            '21CMMC = py21cmmc.cli:main',
        ]
    },
    cffi_modules=["build_cffi.py:ffi"],
)
