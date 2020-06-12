# -*- coding: utf-8 -*-
from collections import OrderedDict

NORM_LIST = [
    ["maj", "M"],
    ["Maj", "M"],
    ["△", "M"],
    ["○", "dim7"],
    ["φ", "m7-5"],
    ["min", "m"],
    ["♭", "b"],
    ["♯", "#"]
]

# parse
ACCIDENTAL = (("#", "+"), ("b", "-"))
ACCIDENTAL_FLAT = "b"
ACCIDENTAL_SHARP = "#"
ACCIDENTAL_VAL = {"#": 1, "b": -1, "+": 1, "-": -1}
ON_CHORD_SIGN = ("/")

# 
SCALE_FLAT = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
SCALE_SHARP = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

NORM_SCALE = {
    "B#": "C",
    "Dbb": "C",
    "C##": "D",
    "Ebb": "D",
    "Fb": "E",
    "D##": "E",
    "E#": "F",
    "F##": "G",
    "Abb": "G",
    "Bbb": "A",
    "G##": "A",
    "Cb": "B",
}

C_MAJOR_SCALE = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
C_SHARP_MAJOR_SCALE = ["C#", "D", "D#", "E", "E#", "F#", "F##", "G#", "A", "A#", "B", "B#"]
D_FLAT_MAJOR_SCALE = ["Db", "Ebb", "Eb", "Fb", "F", "Gb", "G", "Ab", "Bbb", "Bb", "Cb", "C"]
D_MAJOR_SCALE = ["D", "Eb", "E", "F", "F#", "G", "G#", "A", "Bb", "B", "C", "C#"]
E_FLAT_MAJOR_SCALE = ["Eb", "Fb", "F", "Gb", "G", "Ab", "A", "Bb", "Cb", "C", "Db", "D"]
E_MAJOR_SCALE = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]
F_MAJOR_SCALE = ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"]
F_SHARP_MAJOR_SCALE = ["F#", "G", "G#", "A", "A#", "B", "B#", "C#", "D", "D#", "E", "E#"]
G_FLAT_MAJOR_SCALE = ["Gb", "Abb", "Ab", "Bbb", "Bb", "Cb", "C", "Db", "Ebb", "Eb", "Fb", "F"]
G_MAJOR_SCALE = ["G", "Ab", "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#"]
A_FLAT_MAJOR_SCALE = ["Ab", "Bbb", "Bb", "Cb", "C", "Db", "D", "Eb", "Fb", "F", "Gb", "G"]
A_MAJOR_SCALE = ["A", "Bb", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
B_FLAT_MAJOR_SCALE = ["Bb", "Cb", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A"]
B_MAJOR_SCALE = ["B", "C", "C#", "D", "D#", "E", "E#", "F#", "G", "G#", "A", "A#"]
C_FLAT_MAJOR_SCALE = ["Cb", "Dbb", "Ebb", "Eb", "Fb", "F", "Gb", "Abb", "Ab", "Bbb", "Bb"]

A_MINOR_SCALE = ["A", "Bb", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
E_MINOR_SCALE = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]
B_MINOR_SCALE = ["B", "C", "C#", "D", "D#", "E", "E#", "F#", "G", "G#", "A", "A#"]
F_SHARP_MINOR_SCALE = ["F#", "G", "G#", "A", "A#", "B", "B#", "C#", "D", "D#", "E", "E#"]
C_SHARP_MINOR_SCALE = ["C#", "D", "D#", "E", "E#", "F#", "F##", "G#", "A", "A#", "B", "B#"]
G_SHARP_MINOR_SCALE = ["G#", "A", "A#", "B", "B#", "C#", "C##", "D#", "E", "E#", "F#", "F##"]
D_SHARP_MINOR_SCALE = ["D#", "E", "E#", "F#", "F##", "G#", "G##", "A#", "B", "B#", "C#", "C##"]
A_SHARP_MINOR_SCALE = ["A#", "B", "B#", "C#", "C##", "D#", "D##", "E#", "F#", "F##", "G#", "G##"]
D_MINOR_SCALE = ["D", "Eb", "E", "F", "F#", "G", "G#", "A", "Bb", "B", "C", "C#"]
G_MINOR_SCALE = ["G", "Ab", "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#"]
C_MINOR_SCALE = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
F_MINOR_SCALE = ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"]
B_FLAT_MINOR_SCALE = ["Bb", "Cb", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A"]
E_FLAT_MINOR_SCALE = ["Eb", "Fb", "F", "Gb", "G", "Ab", "A", "Bb", "Cb", "C", "Db", "D"]
A_FLAT_MINOR_SCALE = ["Ab", "Bbb", "Bb", "Cb", "C", "Db", "D", "Eb", "Fb", "F", "Gb", "G"]

SCALE_SIG = {
    "C": SCALE_FLAT,
    "D": SCALE_SHARP,
    "E": SCALE_SHARP,
    "F": SCALE_FLAT,
    "G": SCALE_SHARP,
    "A": SCALE_SHARP,
    "B": SCALE_SHARP
}

SCALE = {
    "C": C_MAJOR_SCALE,
    "C#": C_SHARP_MAJOR_SCALE,
    "Db": D_FLAT_MAJOR_SCALE,
    "D": D_MAJOR_SCALE,
    "Eb": E_FLAT_MAJOR_SCALE,
    "E": E_MAJOR_SCALE,
    "F": F_MAJOR_SCALE,
    "Gb": G_FLAT_MAJOR_SCALE,
    "F#": F_SHARP_MAJOR_SCALE,
    "G": G_MAJOR_SCALE,
    "Ab": A_FLAT_MAJOR_SCALE,
    "A": A_MAJOR_SCALE,
    "Bb": B_FLAT_MAJOR_SCALE,
    "B": B_MAJOR_SCALE,
    "Cm": C_MINOR_SCALE,
    "C#m": C_SHARP_MINOR_SCALE,
    "Dm": D_MINOR_SCALE,
    "D#m": D_SHARP_MINOR_SCALE,
    "Ebm": E_FLAT_MINOR_SCALE,
    "Em": E_MINOR_SCALE,
    "Fm": F_MINOR_SCALE,
    "F#m": F_SHARP_MINOR_SCALE,
    "Gm": G_MINOR_SCALE,
    "G#m": G_SHARP_MINOR_SCALE,
    "Abm": A_FLAT_MINOR_SCALE,
    "Am": A_MINOR_SCALE,
    "A#m": A_SHARP_MINOR_SCALE,
    "Bbm": B_FLAT_MINOR_SCALE,
    "Bm": B_MINOR_SCALE,
    "b": SCALE_FLAT,
    "#": SCALE_SHARP,
}

DEGREE = ["I", "bII", "II", "bIII", "III", "IV", "#IV", "V", "bVI", "VI", "bVII", "VII"]

# quality
LABEL_FLAT5 = "b5"
LABEL_FLAT9 = "b9"
LABEL_FLAT13 = "b13"
LABEL_SHARP5 = "#5"
LABEL_SHARP9 = "#9"
LABEL_SHARP11 = "#11"
LABEL_SHARP13 = "#13"
LABEL_2nd = "2"
LABEL_4th = "4"
LABEL_5th = "5"
LABEL_6th = "6"
LABEL_7th = "7"
LABEL_9th = "9"
LABEL_11th = "11"
LABEL_13th = "13"

LABEL_CHORD_PRIORITY = {
    LABEL_FLAT5: 1,
    LABEL_FLAT9: 1,
    LABEL_FLAT13: 1,
    LABEL_SHARP5: 1,
    LABEL_SHARP9: 1,
    LABEL_SHARP11: 1,
    LABEL_SHARP13: 1,
    LABEL_2nd: 2,
    LABEL_4th: 2,
    LABEL_6th: 2,
    LABEL_7th: 2,
    LABEL_9th: 2,
    LABEL_11th: 2,
    LABEL_13th: 2,
}

TENSION = [
    LABEL_FLAT5,
    LABEL_FLAT9,
    LABEL_FLAT13,
    LABEL_SHARP5,
    LABEL_SHARP9,
    LABEL_SHARP11,
    LABEL_SHARP13,
    LABEL_6th,
    LABEL_9th,
    LABEL_11th,
    LABEL_13th]


CHORD_flat5 = 6
CHORD_flat9 = 1
CHORD_flat13 = 8
CHORD_sharp5 = 8
CHORD_sharp9 = 3
CHORD_sharp11 = 6
CHORD_sharp13 = 10
CHORD_major7 = 11

CHORD_root = 0
CHORD_2nd = 2
CHORD_3rd = 4
CHORD_4th = 5
CHORD_5th = 7
CHORD_6th = 9
CHORD_7th = 10
CHORD_9th = 2
CHORD_11th = 5
CHORD_13th = 9


CHORD_VALUE = {
    "1": (-1, CHORD_root),
    "2": (-1, CHORD_2nd),
    "3": (-1, CHORD_3rd),
    "4": (-1, CHORD_4th),
    "5": (-1, CHORD_5th),
    "6": (-1, CHORD_6th),
    "7": (2, CHORD_7th),
    "9": (3, CHORD_9th),
    "11": (4, CHORD_11th),
    "13": (5, CHORD_13th)
}

QUALITY_MAJ = "maj"
QUALITY_MINOR = "m"
QUALITY_MAJOR = "M"
QUALITY_MINOR_MAJOR = "mM"
QUALITY_AUG = 'aug'
QUALITY_AUG_MAJOR = "augM"
QUALITY_DIM = "dim"
QUALITY_ADD = "add"
QUALITY_MINOR_ADD = "madd"
QUALITY_SUS = "sus"

QUALITY_LIST = [QUALITY_MINOR, QUALITY_MAJOR, QUALITY_MINOR_MAJOR, QUALITY_AUG, QUALITY_AUG_MAJOR, QUALITY_DIM, QUALITY_ADD, QUALITY_MINOR_ADD, QUALITY_SUS]
CHORD_QUALITY_MAJOR = (CHORD_root, CHORD_3rd, CHORD_5th, CHORD_7th)
CHORD_QUALITY = {
    QUALITY_MINOR: (0, -1, 0, 0),
    QUALITY_MAJOR: (0, 0, 0, 1),
    QUALITY_MINOR_MAJOR: (0, -1, 0, 1),
    QUALITY_AUG: (0, 0, 1, 0),
    QUALITY_AUG_MAJOR: (0, 0, 1, 1),
    QUALITY_DIM: (0, -1, -1, -1),
    QUALITY_ADD: (0, 0, 0, 0),
    QUALITY_MINOR_ADD: (0, -1, 0, 0),
    QUALITY_SUS: (0, 0, 0, 0),
}

CHORD_MAP = OrderedDict((
    # chords consist of 2 notes
    ('5', (0, 7)),
    # 3 notes
    ('', (0, 4, 7)),
    ('m', (0, 3, 7)),
    ('dim', (0, 3, 6)),
    ('aug', (0, 4, 8)),
    ('sus2', (0, 2, 7)),
    ('sus4', (0, 5, 7)),
    # 4 notes
    ('6', (0, 4, 7, 9)),
    ('7', (0, 4, 7, 10)),
    ('M7', (0, 4, 7, 11)),
    ('m6', (0, 3, 7, 9)),
    ('m7', (0, 3, 7, 10)),
    ('mM7', (0, 3, 7, 11)),
    ('7-5', (0, 4, 6, 10)),
    ('M7-5', (0, 4, 6, 11)),
    ('m7-5', (0, 3, 6, 10)),
    ('mM7-5', (0, 3, 6, 11)),
    ('aug7', (0, 4, 8, 10)),
    ('augM7', (0, 4, 8, 11)),
    ('7sus4', (0, 5, 7, 10)),
    ('dim7', (0, 3, 6, 9)),
    ('add9', (0, 4, 7, 2)),
    ('add11', (0, 4, 7, 5)),
    ('madd9', (0, 3, 7, 2)),

    # 5 notes
    ('69', (0, 4, 7, 9, 2)),
    ('7(9)', (0, 4, 7, 10, 2)),
    ('7(13)', (0, 4, 7, 10, 9)),
    ('7(b9)', (0, 4, 7, 10, 1)),
    ('7(#9)', (0, 4, 7, 10, 3)),
    ('7(#11)', (0, 4, 7, 10, 6)),
    ('7(b13)', (0, 4, 7, 10, 8)),
    ('7-5(9)', (0, 4, 6, 10, 2)),
    ('7-5(#9)', (0, 4, 6, 10, 3)),
    ('7-5(b13)', (0, 4, 6, 10, 8)),
    ('M7(9)', (0, 4, 7, 11, 2)),
    ('M7(13)', (0, 4, 7, 11, 9)),
    ('M7(#11)', (0, 4, 7, 11, 6)),
    ('M7(b9)', (0, 4, 7, 11, 1)),
    ('m69', (0, 3, 7, 9, 2)),
    ('m7(9)', (0, 3, 7, 10, 2)),
    ('m7(11)', (0, 3, 7, 10, 5)),
    ('m7(13)', (0, 3, 7, 10, 9)),
    ('m7(b9)', (0, 3, 7, 10, 1)),
    ('mM7(9)', (0, 3, 7, 11, 2)),
    ('mM7(13)', (0, 3, 7, 11, 9)),
    ('aug9', (0, 4, 8, 10, 2)),

    # 6 notes
    ('7(9, 11)', (0, 4, 7, 10, 2, 5)),
    ('7(9, 13)', (0, 4, 7, 10, 2, 9)),
    ('7(9, #11)', (0, 4, 7, 10, 2, 6)),
    ('7(b9, 13)', (0, 4, 7, 10, 1, 9)),
    ('7(b9, b13)', (0, 4, 7, 10, 1, 8)),
    ('7(b9, #9)', (0, 4, 7, 10, 1, 3)),
    ('7(b9, #11)', (0, 4, 7, 10, 1, 6)),
    ('7(#9, 13)', (0, 4, 7, 10, 3, 9)),
    ('7(#9, b13)', (0, 4, 7, 10, 3, 8)),
    ('7(#9, #11)', (0, 4, 7, 10, 3, 6)),
    ('7(#11, 13)', (0, 4, 7, 10, 6, 9)),
    ('m7(9, 11)', (0, 3, 7, 10, 2, 5)),
    ('m7(9, 13)', (0, 3, 7, 10, 2, 9)),
    ('M7(9, 11)', (0, 4, 7, 11, 2, 5)),
    ('M7(9, 13)', (0, 4, 7, 11, 2, 9)),

    # 7 notes
    ('7(9, 11, 13)', (0, 4, 7, 10, 2, 5, 9)),
    ('7(b9, #11, 13)', (0, 4, 7, 10, 1, 6, 9)),
    ('m7(9, 11, 13)', (0, 3, 7, 10, 2, 5, 9)),
    ('M7(9, 11, 13)', (0, 4, 7, 11, 2, 5, 9)),

))
