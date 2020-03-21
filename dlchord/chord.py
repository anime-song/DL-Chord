# -*- coding: utf-8 -*-
from .const import ACCIDENTAL, ON_CHORD_SIGN, ACCIDENTAL_FLAT, ACCIDENTAL_SHARP
from .const import SCALE_FLAT, SCALE_SHARP, SCALE_SIG, SCALE, DEGREE
from .const import NORM_LIST
from .const import QUALITY_AUG, QUALITY_MINOR, QUALITY_SUS
from .const import LABEL_5th, LABEL_6th, LABEL_7th
from .quality import Quality
from .util import note_to_value, value_to_note, relative_value, c_shift
from .parser import note_to_chord


def normalize(chord):
    for key in NORM_LIST:
        chord.replace(key[0], key[1])
    return chord


def parse(chord):
    accidental = ""
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
            accidental = ACCIDENTAL_SHARP
            
        elif chord[1] in ACCIDENTAL[1]:
            scale = SCALE_FLAT
            accidental = ACCIDENTAL_FLAT
            
        else:
            scale = SCALE_SIG[chord[0]]
        
        root = scale[note_to_value(root)]
    elif len(chord) > 0:
        scale = SCALE_SIG[chord[0]]
        root = chord[:1]
        rest = chord[1:]

    on_chord_index = rest.find(ON_CHORD_SIGN)
    if on_chord_index >= 0:
        on = rest[on_chord_index + 1:]
        rest = rest[:on_chord_index]
    else:
        on = None

    quality = Quality(rest)

    return root, quality, on, scale, accidental


class Chord:
    """コードを処理するクラス
    
    """
    def __init__(self, chord):
        chord = normalize(chord)
        self._chord = chord
        try:
            self._root, self._quality, self._on, self._scale, self._accidental = parse(self._chord)
        
        except Exception:
            raise ValueError(
                "Could not parse Chord. Invalid Chord {}".format(self.chord))
      
        if self._root not in self._scale:
            raise ValueError(
                "Could not parse Chord. Invalid Chord {}".format(self.chord))


    def __unicode__(self):
        return self._chord
        
    def __str__(self):
        return self._chord

    def __repr__(self):
        return "<Chord: {}>".format(self._chord)

    def __lt__(self, other):
        if not isinstance(other, Chord):
            raise TypeError("Cannot compare Chord object with {} object".format(type(other)))
        
        if self.quality.quality == LABEL_5th:
            return True

        if QUALITY_SUS in self.quality.quality and ON_CHORD_SIGN in self.chord:
            return True

        if "omit" in self.quality.quality:
            return True

        if self.quality.quality == QUALITY_AUG and other.quality.quality == QUALITY_AUG:
            if ON_CHORD_SIGN in other.chord and ON_CHORD_SIGN in self.chord:
                if (other.bass - other.root) % 12 == 6:
                    return True
        if ON_CHORD_SIGN not in other.chord and ON_CHORD_SIGN in self.chord:
            return True
        elif ON_CHORD_SIGN in other.chord and ON_CHORD_SIGN not in self.chord:
            return False

        if LABEL_6th in self.quality.quality and (QUALITY_MINOR + LABEL_7th) in other.quality.quality:
            return True

        elif (QUALITY_MINOR + LABEL_7th) in self.quality.quality and LABEL_6th in other.quality.quality:
            return False

        if self.bass in Chord(value_to_note(self.root) + self.quality.quality).getNotes():
            return True

        return False

    def __ge__(self, other):
        return not self.__le__(other)

    def __eq__(self, value):
        if not isinstance(value, Chord):
            raise TypeError("Cannot compare Chord object with {} object".format(type(value)))

        if not all(value.getNotes(categorical=True) == self.getNotes(categorical=True)):
            return False
        
        return True

    def __ne__(self, value):
        return not self.__eq__(value)

    @property
    def chord(self):
        return self._chord

    @property
    def quality(self):
        return self._quality

    @property
    def accidental(self):
        return self._accidental

    @property
    def root(self):
        """ルート音を取得します。

        Examples
        --------
        >>> from dlchord import Chord
        >>> chord = Chord("C")
        >>> print(chord.root())

        0

        >>> from dlchord import Chord
        >>> chord = Chord("C/G")
        >>> print(chord.root())

        0
        """

        num = note_to_value(self._root)

        return num

    @property
    def bass(self):
        """ベース音を取得します。

        Examples
        --------
        >>> from dlchord import Chord
        >>> chord = Chord("C")
        >>> print(chord.bass())

        0

        >>> from dlchord import Chord
        >>> chord = Chord("C/G")
        >>> print(chord.bass())

        7
        """
        if self._on is not None:
            num = note_to_value(self._on)
        else:
            num = note_to_value(self._root)

        return num

    @property
    def onchord(self):
        return self._on

    @property
    def isOnchord(self):
        if self._on is not None:
            return True
        else:
            return False

    def getNotes(self, categorical=False):
        """コードの構成音を取得します。

        Parameters
        ----------
        categorical : boolean
            12個に分解するかどうか
        
        Examples
        --------
        >>> from dlchord import Chord
        >>> chord = Chord("C")
        >>> cons = chord.getNotes(categorical=False)
        >>> print(str(cons))

        [0 4 7]

        >>> cons = chord.getNotes(categorical=True)
        >>> print(str(cons))

        [2. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 0.]

        ベース音 2
        構成音 1
        非構成音 0

        Returns
        -------
        chord notes: [notes]

        """
        notes = self._quality.getNotes(root=self._root, on=self._on, categorical=categorical)
        return notes

    def components(self):
        """コードの構成音を文字で取得します。

        Examples
        --------
        >>> from dlchord import Chord
        >>> chord = Chord("C")
        >>> comp = chord.components()
        >>> comp

        ["C", "E", "G"]

        >>> chord = Chord("C#")
        >>> comp = chord.components()
        >>> comp

        ["C#", "F", "G#"]

        """
        notes = self.getNotes()
        comp = [self._scale[note] for note in notes]

        return comp

    def transpose(self, steps):
        """コードを移調します。
        
        Parameters
        ----------
            steps : int
                移調する数


        Examples
        --------
        >>> from dlchord import Chord
        >>> chord = Chord("C")
        >>> t_chord = chord.transpose(steps=1)
        >>> print(str(t_chord))
        Db
        
        Returns:
            Chord : Chord
                移調後のコード
        """
        root_num = note_to_value(self._root)
        root = self._scale[(root_num + steps) % len(self._scale)]
        on = ''

        if self._on is not None:
            on_num = note_to_value(self._on)
            on = ON_CHORD_SIGN + \
                self._scale[(on_num + steps) % len(self._scale)]

        t_chord = Chord(root + str(self._quality) + on)

        return t_chord

    def degree(self, key=0):
        """
        
        Parameters
        ----------
            key : int
                基準とする調
                C = 0
        
        Examples
        --------
        >>> from dlchord import Chord
        >>> chord = Chord("C")
        >>> print(chord.degree(key=0)) # C調
        I

        Returns:
            degree : str
        """
        
        root_n = self._scale.index(self._root)

        degr = DEGREE[root_n - key]
        on = ON_CHORD_SIGN + self._on if self._on is not None else ""

        return degr + str(self._quality) + on

    def modify(self, key="C", advanced=False):
        """コードを修正します。

        Examples
        --------
        >>> from dlchord import Chord
        >>> chord = Chord("E/Ab")
        >>> chord.modify()
        E/G#

        >>> chord = Chord("AM7/F#")
        >>> chord.modify()
        F#m7(9)

        Returns:
            chord : Chord
        """

        chord = note_to_chord(self.getNotes(), scale=key, advanced=advanced)[0]
        
        if chord.isOnchord:
            if Chord(chord.onchord).accidental != "":
                if chord.accidental:
                    if chord.accidental != Chord(chord.onchord).accidental:
                        chord = Chord(
                            chord.chord.split(ON_CHORD_SIGN)[0] +
                            ON_CHORD_SIGN +
                            Chord(chord.onchord).modify(chord.accidental).chord)
                else:
                    if QUALITY_AUG not in chord.quality.quality:
                        chord = Chord(
                            chord.chord.split(ON_CHORD_SIGN)[0] +
                            ON_CHORD_SIGN +
                            c_shift(SCALE[chord.chord[0]])[chord.bass])

        return chord
