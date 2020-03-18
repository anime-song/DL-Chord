# -*- coding: utf-8 -*-
from .const import ACCIDENTAL, ACCIDENTAL_VAL, ACCIDENTAL_FLAT, ACCIDENTAL_SHARP
from .const import SCALE_FLAT, SCALE_SHARP, SCALE
from .parser import find_chord, c_shift
import numpy as np


def note_to_chord(notes, scale="C", advanced=False):
    """構成音からコードを推定します。
    
    Parameters
    ----------

    notes : list (int or str)
        構成音のリスト

    scale : str
        コードのスケール
        

    Examples
    --------
    >>> from dlchord import note_to_chord
    >>> chords = note_to_chord(["C", "E", "G"])
    >>> chords
    [<Chord : C>]

    >>> from dlchord import note_to_chord
    >>> chords = note_to_chord([0, 4, 7])
    >>> chords
    [<Chord: C>]

    >>> chords = note_to_chord(["B", "Db", "F", "A"])
    >>> chords
    [<Chord: Faug/B>, <Chord: Dbaug/B>, <Chord: Aaug/B>]

    >>> chords = note_to_chord(["B", "Db", "F", "A"], scale="F#")
    >>> chords
    [<Chord: Faug/B>, <Chord: C#aug/B>, <Chord: Aaug/B>]
    """
    notes = list(notes)
    if not list(notes):
        raise ValueError("Please specify notes which consist a chord.")
    
    norm_notes = []

    for note in notes:
        if type(note) is str:
            norm_notes.append(note_to_value(note))
        else:
            if type(note) is int or isinstance(note, np.intc):
                norm_notes.append(note % 12)
            else:
                raise ValueError("notes must be an integer or string.")

    bass = norm_notes[0]

    norm_notes = sorted(list(set(norm_notes)))
    norm_notes.remove(bass)
    norm_notes.insert(0, bass)

    chord_list = find_chord(
        norm_notes,
        bass=bass,
        scale=scale,
        advanced=advanced)

    return chord_list


def note_to_value(note):
    if note is None or not type(note) is str:
        raise ValueError("Invalid note {}".format(note))

    if note[:1] not in SCALE_FLAT:
        raise ValueError("Unknown note {}".format(note))

    # key = _norm(key)

    if any((s in note) for s in ACCIDENTAL[0]):
        scale_number = SCALE_SHARP
    elif any((s in note) for s in ACCIDENTAL[1]):
        scale_number = SCALE_FLAT
    else:
        scale_number = SCALE_FLAT

    if len(note) > 2:
        result_num = scale_number.index(
            note[:1]) + ACCIDENTAL_VAL[note[1]] + ACCIDENTAL_VAL[note[2]]
    elif len(note) > 1:
        result_num = scale_number.index(note[:1]) + ACCIDENTAL_VAL[note[1]]
    else:
        result_num = scale_number.index(note)

    result_num = result_num % len(SCALE_FLAT)

    return result_num


def relative_value(value, key):
    return (value - note_to_value(key)) % 12


def value_to_note(value, scale="C"):
    if value is None or not any([type(value) is int, isinstance(value, np.intc)]):
        raise ValueError("Invalid value {}".format(value))

    value %= 12

    if SCALE.get(scale):
        return c_shift(SCALE[scale])[value]
    else:
        raise ValueError("value must be sharp or flat")


def to_categorical(x, classes=12):
    y = np.zeros((classes))
    y[x[0]] = 2
    for i in range(1, len(x)):
        y[x[i]] = 1

    return y
