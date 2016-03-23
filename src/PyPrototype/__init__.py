
# Copyright (c) 2009 - 2016, UChicago Argonne, LLC.
# See LICENSE file for details.

'''
Source code for the PyPrototype package
'''

'''
Will it be necessary to add this next line at the top of every file?
# -*- coding: iso-8859-1 -*- 
'''

__package_name__        = u'PyPrototype'
__description__         = u'prototype repository of a Python project'
__long_description__    = __description__

#__version__             = u'2016.0113.0'
# set the version by tagging a commit in git
__author__              = u'Pete R. Jemian'
__email__               = u'jemian@anl.gov'
__institution__         = u"Advanced Photon Source, Argonne National Laboratory"
__settings_orgName__    = u'Advanced_Photon_Source'
__author_name__         = __author__
__author_email__        = __email__

__copyright__           = u'2011-2016, UChicago Argonne, LLC'
# __license_url__         = u''
__license__             = u'UChicago Argonne, LLC OPEN SOURCE LICENSE (see LICENSE file)'
__url__                 = u'http://PyPrototype.readthedocs.org'
__download_url__        = u'https://github.com/prjemian/PyPrototype.git'
__keywords__            = ['APS', 'science']
#__requires__            = ['PyQt4', 'lxml', 'pyRestTable']
__requires__            = []
__documentation_mocks__ = []       # do NOT mock PyQt4 here, big problems if you do

__classifiers__ = [
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Science/Research',
            'License :: Free To Use But Restricted',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Topic :: Utilities',
                     ]

# as shown in the About box ...
__credits__ = u'author: ' + __author__
__credits__ += u'\nemail: ' + __email__
__credits__ += u'\ninstitution: ' + __institution__
__credits__ += u'\nURL: ' + __url__


from _version import get_versions
__version__ = get_versions()['version']
del get_versions

import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    # special handling for readthedocs.org, remove distracting info
    __version__ = __version__.split('+')[0]
__release__             = __version__
