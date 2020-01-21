# -*- coding: utf-8 -*-
from .const import ACCIDENTAL_FLAT, ACCIDENTAL_SHARP
from .const import SCALE_FLAT, SCALE_SHARP
from .const import CHORD_MAP
from .const import CHORD_3rd, CHORD_5th
from .const import LABEL_5th
from .const import ON_CHORD_SIGN
from .const import QUALITY_AUG
from . import chord


def _match_count(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] in b:
            count += 1
    return count


def _find_quality(notes):
    count_list = []
    quality = []
    sorted_notes = sorted(notes)
    for q, p in CHORD_MAP.items():
        p = sorted(list(p))
        if sorted_notes == p:
            quality.append(q)

        count_list.append([_match_count(sorted_notes, p), q])

    if quality:
        return quality, True
    
    count_list = sorted(count_list, key=lambda x: x[0], reverse=True)
    quality.append(count_list[0][1])

    return quality, False


def _rotate_notes(notes):
    for x in range(len(notes)):
        yield notes[x:] + notes[:x]


def find_chord(notes, bass, scale="b"):
    if scale == ACCIDENTAL_FLAT:
        scale = SCALE_FLAT
    elif scale == ACCIDENTAL_SHARP:
        scale = SCALE_SHARP
    else:
        raise ValueError("scale must be sharp or flat.")

    chord_list = []
    root = ""
    quality = ""

    rel_notes = [(note - notes[0]) % 12 for note in notes]
    match = False

    for rotated in _rotate_notes(rel_notes[1:]):
        rel_rotated_notes = [(note - rotated[0]) % 12 for note in rotated]
        quality, match = _find_quality(rel_rotated_notes)

        if match:
            root_num = (rotated[0] + bass) % 12
            root = scale[root_num]
            if root_num != bass:
                onchord = ON_CHORD_SIGN + scale[bass]
            else:
                onchord = ""
            
            for q in quality:
                chord_list.append(chord.Chord(root + q + onchord))

    for rotated in _rotate_notes(rel_notes):
        rel_rotated_notes = [(note - rotated[0]) % 12 for note in rotated]
        quality, match = _find_quality(rel_rotated_notes)

        if match:
            root_num = (rotated[0] + bass) % 12
            root = scale[root_num]
            if root_num != bass:
                onchord = ON_CHORD_SIGN + scale[bass]
            else:
                onchord = ""

            for q in quality:
                chord_list.append(chord.Chord(root + q + onchord))

    return sorted(chord_list, reverse=True)
