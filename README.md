# DL-Chord

## 概要
コードを解析するライブラリ。
コード構成音の解析や、移調、ディグリーなどが使用可能です。

## インストール
```sh
$ pip install dlchord
```

## コード読み込み
```python
>>> from dlchord import Chord
>>> chord = Chord("C")
>>> print(str(chord))
C
```

## ルート音取得
```python
>>> from dlchord import Chord
>>> chord = Chord("C")
>>> print(chord.getroot())
1

>>> from dlchord import Chord
>>> chord = Chord("C/G")
>>> print(chord.getroot())

1
```

## ベース音取得
```python
>>> from dlchord import Chord
>>> chord = Chord("C")
>>> print(chord.getbass())
1

>>> from dlchord import Chord
>>> chord = Chord("C/G")
>>> print(chord.getbass())

8
```


## 移調
```python
>>> from dlchord import Chord
>>> chord = Chord("C")
>>> t_chord = chord.transpose(steps=1)
>>> print(str(t_chord))
Db
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
[1 5 8]

>>> cons = chord.getNotes(categorical=True)
>>> print(str(cons))
[2. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 0.]
# ルート音 2
# 構成音 1
# 非構成音 0
```
