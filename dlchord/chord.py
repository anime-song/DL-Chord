from .const import ACCIDENTAL, ON_CHORD_SIGN, SCALE_FLAT, SCALE_SHARP, DEGREE
from .quality import Quality, keynumber


def normalize(chord):
    return chord.replace(
        "maj",
        "M").replace(
        "△",
        "M").replace(
            "○",
        "dim7").replace("φ", "m7-5")


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
        chord = normalize(chord)
        self._chord = chord
        self._root, self._quality, self._on, self._scale = parse(self._chord)
      
        if self._root not in self._scale:
            raise ValueError(
                "The Chord could not be parsed. It may not be in the correct format.")

    def __str__(self):
        return self._chord

    def getNotes(self, norm=False, categorical=False):
        """コードの構成音を取得します。

        Parameters
        ----------
        norm : boolean
            最大値で正規化するかどうか

        categorical : boolean
            12個に分解するかどうか
        
        Examples
        --------
        >>> from dlchord import Chord
        >>> chord = Chord("C")
        >>> cons = chord.getNotes(categorical=False)
        >>> print(str(cons))

        [1 5 8]

        >>> cons = chord.getNotes(categorical=True)
        >>> print(str(cons))

        [2. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 0.]

        ルート音 2
        構成音 1
        非構成音 0

        Returns
        -------
        chord notes: [notes]

        """
        return self._quality.getNotes(
            root=self._root, on=self._on, norm=norm, categorical=categorical)
    
    def getroot(self):
        """ルート音を取得します。
        
        Examples
        --------
        >>> from dlchord import Chord
        >>> chord = Chord("C")
        >>> print(chord.getroot())

        1

        >>> from dlchord import Chord
        >>> chord = Chord("C/G")
        >>> print(chord.getroot())

        1
        """

        num = keynumber(self._root)

        return num + 1

    def getbass(self):
        """ベース音を取得します。

        Examples
        --------
        >>> from dlchord import Chord
        >>> chord = Chord("C")
        >>> print(chord.getbass())

        1

        >>> from dlchord import Chord
        >>> chord = Chord("C/G")
        >>> print(chord.getbass())

        8
        """
        if self._on is not None:
            num = keynumber(self._on)
        else:
            num = keynumber(self._root)

        return num + 1

    def transpose(self, steps):
        """
        
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
            Chord : pywfd.Chord
                移調後のコード
        """
        root_num = keynumber(self._root)
        root = self._scale[(root_num + steps) % len(self._scale)]
        on = ''

        if self._on is not None:
            on_num = keynumber(self._on)
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
