from .const import ACCIDENTAL, ON_CHORD_SIGN, SCALE_FLAT, SCALE_SHARP, DEGREE, QUALITY_LIST
from .quality import Quality, keynumber


def parse(chord):

    if len(chord) > 1 and any((chord[1] in acc) for acc in ACCIDENTAL):
        if len(chord) > 2:
            if any((chord[2] in acc) for acc in ACCIDENTAL):
                root = chord[:3]
                rest = chord[3:]
            else:
                root = chord[:2]
                rest = chord[2:]
        else:
            root = chord[:2]
            rest = chord[2:]
        
        if chord[1] in ACCIDENTAL[0]:
            scale = SCALE_SHARP
            root = SCALE_SHARP[keynumber(root)]
        else:
            scale = SCALE_FLAT
            root = SCALE_FLAT[keynumber(root)]

    else:
        scale = SCALE_FLAT
        root = chord[:1]
        rest = chord[1:]

    on_chord_index = rest.find(ON_CHORD_SIGN)
    if on_chord_index >= 0:
        on = rest[on_chord_index + 1:]
        rest = rest[:on_chord_index]
    else:
        on = None

    quality = Quality(rest)

    return root, quality, on, scale


class Chord:

    def __init__(self, chord):
        self._chord = chord

        self._root, self._quality, self._on, self._scale = parse(self._chord)

        quality_name, _ = self._quality._getQuality(
            self._quality._quality)
        
        if quality_name == "":
            raise ValueError(
                "The Chord could not be parsed. It may not be in the correct format.")

    def __str__(self):
        return self._chord

    def getnumber(self, norm=False):
        """[summary]
        
        Returns:
            [ndarray]: [chord number]
        """
        return self._quality.getnumber(root=self._root, on=self._on, norm=norm)
    
    def getfeature(self):
        num = keynumber(self._root) + 1
        return num

    def transpose(self, key):
        root_num = keynumber(self._root)
        root = self._scale[(root_num + key) % len(self._scale)]
        on = ''

        if self._on is not None:
            on_num = keynumber(self._on)
            on = ON_CHORD_SIGN + self._scale[(on_num + key) % len(self._scale)]

        t_chord = Chord(root + str(self._quality) + on)

        return t_chord

    def degree(self, key=0):
        
        root_n = self._scale.index(self._root)

        degr = DEGREE[root_n - key]
        on = ON_CHORD_SIGN + self._on if self._on is not None else ""

        return degr + str(self._quality) + on
