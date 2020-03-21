# -*- coding: utf-8 -*-
from .const import ACCIDENTAL, ACCIDENTAL_VAL, ACCIDENTAL_FLAT, ACCIDENTAL_SHARP
from .const import SCALE_FLAT, SCALE_SHARP, SCALE
import numpy as np


def c_shift(arr):
    value_arr = [note_to_value(v) for v in arr]
    n = value_arr.index(0)
    return arr[n:] + arr[:n]


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
    y = np.zeros((classes), dtype="float32")
    y[x[0]] = 2
    for i in range(1, len(x)):
        y[x[i]] = 1

    return y
