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


class MyGui(QtGui.QWidget):
    '''
    Creates a Qt widget in a window
    '''

    def __init__(self, message, filename):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QFormLayout()
        self.setLayout(layout)

        w_msg = QtGui.QLabel(self)
        w_msg.setText(message)

        w_fn = QtGui.QLabel(self)
        w_fn.setText(str(filename))
        layout.addRow(w_msg, w_fn)


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
    import sys
    parms = process_command_line()
    app = QtGui.QApplication(sys.argv)
    message = "HDF file:"
    win = MyGui(message, parms.infile)
    win.show()
    _r = app.exec_()
    sys.exit(_r)


if __name__ == '__main__':
    main()
