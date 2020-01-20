# DL-Chord

## 概要
コードを解析するライブラリ。
コード構成音の解析や、移調、ディグリーなどが使用可能です。

## インストール
```sh
$ pip install dlchord
```

## コード作成
```python
>>> from dlchord import Chord
>>> chord = Chord("C")
>>> chord
<Chord: C>
```

## コード検索
```python
>>> from dlchord import note_to_chord
>>> chords = note_to_chord(["C", "E", "G"])
>>> chords
[<Chord : C>]

>>> chords = note_to_chord(["B", "Db", "F", "A"])
>>> chords
[<Chord: Faug/B>, <Chord: Dbaug/B>, <Chord: Aaug/B>]

>>> chords = note_to_chord(["B", "Db", "F", "A"], scale="#")
>>> chords
[<Chord: Faug/B>, <Chord: C#aug/B>, <Chord: Aaug/B>]
```

## ルート音取得
```python
>>> from dlchord import Chord
>>> chord = Chord("C")
>>> print(chord.root())
0

>>> from dlchord import Chord
>>> chord = Chord("C/G")
>>> print(chord.root())

0
```

## ベース音取得
```python
>>> from dlchord import Chord
>>> chord = Chord("C")
>>> print(chord.bass())
0

>>> from dlchord import Chord
>>> chord = Chord("C/G")
>>> print(chord.bass())

7
```


## 移調
```python
>>> from dlchord import Chord
>>> chord = Chord("C")
>>> t_chord = chord.transpose(steps=1)
>>> t_chord
<Chord: Db>
```

## ディグリー
```python
>>> from dlchord import Chord
>>> chord = Chord("C")
>>> print(chord.degree(key=0)) # C調
I
```


## 構成音取得
```python
>>> from dlchord import Chord
>>> chord = Chord("C")
>>> cons = chord.getNotes(categorical=False)
>>> print(str(cons))
[0 4 7]

>>> cons = chord.getNotes(categorical=True)
>>> print(str(cons))
[2. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 0.]
# ベース音 2
# 構成音 1
# 非構成音 0
```

## コードを比較
```python
>>> from dlchord import Chord
>>> Chord("C") == Chord("C")
True
>>> Chord("C") == Chord("C7")
False
>>> Chord("C#") == Chord("Db")
True
>>> Chord("F/D") == Chord("Dm7")
True
>>> Chord("C#dim7/A") == Chord("A7(b9)")
True
```