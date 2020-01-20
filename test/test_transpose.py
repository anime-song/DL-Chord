# -*- coding: utf-8 -*-
import unittest

from dlchord import Chord


class TestTranspose(unittest.TestCase):
    def test_transpose_zero(self):
        c = Chord("Am")
        t = c.transpose(0)
        self.assertEqual(t, Chord("Am"))

    def test_transpose_positive(self):
        c = Chord("Am")
        t = c.transpose(3)
        self.assertEqual(t, Chord("Cm"))

    def test_transpose_negative(self):
        c = Chord("Am")
        t = c.transpose(-3)
        self.assertEqual(t, Chord("F#m"))

    def test_transpose_slash(self):
        c = Chord("Am/G")
        t = c.transpose(3)
        self.assertEqual(t, Chord("Cm/Bb"))


if __name__ == '__main__':
    unittest.main()
