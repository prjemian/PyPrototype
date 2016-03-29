
'''
This module is *only* for building the documentation at readthedocs.org
'''

class QMockObject(object):
    '''hide Qt classes from ReadTheDocs'''
    def __init__(self, *args, **kwargs):
        super(QMockObject, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return None

class loadUi(QMockObject): pass
