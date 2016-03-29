#!/usr/bin/env python

# Copyright (c) 2009 - 2016, UChicago Argonne, LLC.
# See LICENSE file for details.

'''
:mod:`main_gui.Main` code runs the GUI.

usage::

    python main_gui.py [input_file]

'''

import os
#import sys
#import traceback

ON_RTD = os.environ.get('READTHEDOCS', None) == 'True'
if not ON_RTD:
    from PyQt4 import QtCore, QtGui
else:
    from mock_PyQt4 import QtCore, QtGui

import __init__


def process_command_line():
    '''
    support command-line options such as ```--help``` and ```--version```
    '''
    import argparse
    doc = __init__.__doc__
    version = __init__.__version__
    doc = 'v' + version + ', ' + doc.strip()
    parser = argparse.ArgumentParser(description=doc)
    parser.add_argument('-v', '--version', action='version', version=version)
    parser.add_argument(
        'infile',
        action='store',
        nargs='?',
        help="HDF5 data file name (optional)",
        default=None)
    # if we get here, then OK to proceed to start program
    return parser.parse_args()


def main():
    '''start the program'''
    parms = process_command_line()
    print "Hello, World.  You'll need to write the GUI.  input file: ",
    print parms.infile


if __name__ == '__main__':
    main()
