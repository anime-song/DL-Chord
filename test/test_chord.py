# -*- coding: utf-8 -*-
import unittest

from dlchord import Chord
from dlchord.util import note_to_chord


class TestChord(unittest.TestCase):

    def test_major(self):
        chord = note_to_chord(["C", "E", "G"])[0]
        self.assertEqual(chord, Chord("C"))

    def test_seventh(self):
        chord = note_to_chord(["C", "E", "G", "Bb"])[0]
        self.assertEqual(chord, Chord("C7"))

    def test_ninth(self):
        chord = note_to_chord(["C", "E", "G", "Bb", "D"])[0]
        self.assertEqual(chord, Chord("C7(9)"))

    def test_eleventh(self):
        chord = note_to_chord(["C", "E", "G", "Bb", "D", "F"])[0]
        self.assertEqual(chord, Chord("C7(9, 11)"))

    def test_add9(self):
        chord = note_to_chord(["C", "E", "G", "D"])[0]
        self.assertEqual(chord, Chord("Cadd9"))


if __name__ == '__main__':
    unittest.main()
