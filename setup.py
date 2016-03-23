#!/usr/bin/env python

# Copyright (c) 2011 - 2016, UChicago Argonne, LLC.
# See LICENSE file (in src/PyPrototype) for details.


from setuptools import setup, find_packages
import os
import re
import sys
import versioneer

# pull in some definitions from the package's __init__.py file
sys.path.insert(0, os.path.join('src', ))
import PyPrototype

requires = PyPrototype.__requires__
packages = find_packages()
verbose=1
long_description = open('README.rst', 'r').read()


setup (name             = PyPrototype.__package_name__,        # PyPrototype
       version=versioneer.get_version(),
       cmdclass=versioneer.get_cmdclass(),
       #version          = PyPrototype.__version__,
       license          = PyPrototype.__license__,
       description      = PyPrototype.__description__,
       long_description = long_description,
       author           = PyPrototype.__author_name__,
       author_email     = PyPrototype.__author_email__,
       url              = PyPrototype.__url__,
       download_url     = PyPrototype.__download_url__,
       keywords         = PyPrototype.__keywords__,
       install_requires = requires,
       platforms        = 'any',
       package_dir      = {'PyPrototype': 'src/PyPrototype'},
       #packages         = find_packages(),
       packages         = [str(PyPrototype.__package_name__), 
                           # do not really need to package this mock
                           'PyPrototype.mock_PyQt4',
                           ],
       package_data     = dict(PyPrototype=['resources/*', 
                                           'LICENSE', ]),
       classifiers      = PyPrototype.__classifiers__,
       entry_points={
            # create & install console_scripts in <python>/bin
            # 'console_scripts': [
            #   'PyPrototype=PyPrototype.main:main', 
            # ],
            'gui_scripts': ['PyPrototype=PyPrototype.main_gui:main'],
      },
  )
