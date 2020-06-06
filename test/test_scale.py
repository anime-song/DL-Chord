# -*- coding: utf-8 -*-
import unittest

from dlchord.chord import Chord
from dlchord.const import SCALE


class TestScale(unittest.TestCase):
    def test_length(self):
        for k, scale in SCALE.keys():
            self.assertEqual(len(scale), 12)

    def test_duplicates(self):
        for k, scale in SCALE.keys():
            self.assertTrue(len(scale) != len(set(scale)))

    def test_notes(self):
        notes = list(range(12))
        for k, scale in SCALE.keys():
            scale = sorted([Chord(note).bass for note in scale])

            self.assertEqual(notes, scale)


if __name__ == '__main__':
    unittest.main()
