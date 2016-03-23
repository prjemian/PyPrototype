How to Install *PyPrototype*
############################

The basic installation procedure:

#. install Python 2.7
#. install PyPrototype

Background
**********

This program requires Python 2.7 (not ready for Python 3 yet)
and several additional packages.  Most of the package dependencies
are met by using a Python distribution (provides Python, the basic 
package suite, and other popular packages).

The major package requirements are:

* *PyQt4* : provides the graphical user interface widgets

Python
******

It is suggested to use the Anaconda Python 2.7 distribution [#]_ as it
contains most of the packages used by this program.

#. use a web browser and visit: https://www.continuum.io/downloads
#. select the distribution for your operating system 
#. make sure to follow links for *Python 2.7*
#. download the installer file
#. follow the instructions to install on your computer

.. [#] Anaconda Python 2.7: https://www.continuum.io

*PyPrototype*
*************

Install this program from the Python Package Index (PyPI) 
using the *pip* command::

    pip install pyRestTable
    pip install --no-deps PyPrototype

The ``--no-deps`` option tells *pip* not to download and attempt 
to build newer versions of other required packages such as *lxml*.

It *may* be necessary to install the *lxml* package if your distribution
does not already have it installed.  You can view all the installed
packages using this command::

    pip list

The list may have dozens or more items.  To install *lxml*::

    pip install lxml

Updating *PyPrototype*
----------------------

To update to a newer version of *PyPrototype*, use this command::

    pip install -U --no-deps PyPrototype

The ``-U`` option tells *pip* to search for and install the 
latest package update.

Alternative Installation steps
------------------------------

It is possible to install **PyPrototype** using steps 
common to Python developers, such as::

     pip install https://github.com/prjemian/PyPrototype

or::

    git clone install https://github.com/prjemian/PyPrototype.git
    cd pyprototype
    python ./setup.py install

Working from a GitHub clone is not recommended for regular use.
