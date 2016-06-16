import doctest
import sys


if sys.version_info >= (3,):
    def load_tests(loader, tests, ignore):
        return doctest.DocFileSuite('../README.rst')
