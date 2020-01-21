# -*- coding: utf-8 -*-
import unittest

from dlchord.chord import Chord
from dlchord.util import note_to_chord


class TestChord(unittest.TestCase):
    
    def test_power(self):
        chord = note_to_chord(["E", "G", "C"])[0]
        self.assertEqual(chord, Chord("C/E"))

    def test_major(self):
        chord = note_to_chord(["C", "E", "G"])[0]
        self.assertEqual(chord, Chord("C"))
    
    def test_major7th(self):
        chord = note_to_chord(["C", "E", "G", "B"])[0]
        self.assertEqual(chord, Chord("CM7"))

    def test_7th(self):
        chord = note_to_chord(["C", "E", "G", "Bb"])[0]
        self.assertEqual(chord, Chord("C7"))

    def test_9th(self):
        chord = note_to_chord(["C", "E", "G", "Bb", "D"])[0]
        self.assertEqual(chord, Chord("C7(9)"))

    def test_11th(self):
        chord = note_to_chord(["C", "E", "G", "Bb", "D", "F"])
        self.assertEqual(chord[0], Chord("C7(9, 11)"))

    def test_add9(self):
        chord = note_to_chord(["C", "E", "G", "D"])[0]
        self.assertEqual(chord, Chord("Cadd9"))

    def test_slash1(self):
        chord = note_to_chord(["D", "C", "E", "G"])[0]
        self.assertEqual(chord, Chord("C/D"))

    def test_slash2(self):
        chord = note_to_chord(["C", "A", "C", "E", "F#"])[0]
        self.assertEqual(chord, Chord("F#m7-5/C"))

    def test_slash3(self):
        chord = note_to_chord(["C", "Gb", "Bb", "D"])[0]
        self.assertEqual(chord, Chord("Gbaug/C"))

    def test_7th_integer(self):
        chord = note_to_chord([0, 4, 7, 10])[0]
        self.assertEqual(chord, Chord("C7"))


if __name__ == '__main__':
    unittest.main()
