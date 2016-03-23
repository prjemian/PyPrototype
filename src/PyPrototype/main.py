#!/usr/bin/env python

# Copyright (c) 2009 - 2016, UChicago Argonne, LLC.
# See LICENSE file for details.

'''
:mod:`Main` code runs the command-line program.

usage::

    python main.py [input_file]

'''

import os, sys

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
    parser.add_argument('infile', 
                        action='store', 
                        nargs='?', 
                        help="HDF5 data file name (optional)",
                        default=None)
    return parser.parse_args()  # if we get here, then OK to proceed to start program


def main():
    '''start the program'''
    parms = process_command_line()
    print 'Hello, World.  input file: ', parms.infile


if __name__ == '__main__':
    main()
