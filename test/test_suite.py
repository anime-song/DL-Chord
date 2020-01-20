import unittest

from . import test_transpose
from . import test_chord


def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_transpose.TestTranspose())
    suite.addTest(test_chord.TestChord())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
