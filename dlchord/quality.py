# -*- coding: utf-8 -*-
from .const import LABEL_CHORD_PRIORITY, TENSION, LABEL_7th
from .const import CHORD_QUALITY, CHORD_QUALITY_MAJOR
from .const import ACCIDENTAL, ACCIDENTAL_FLAT, ACCIDENTAL_SHARP
from .const import QUALITY_SUS, QUALITY_ADD, QUALITY_MINOR_ADD
from .const import CHORD_VALUE
from .const import CHORD_root, CHORD_3rd, CHORD_5th
from .util import note_to_value, to_categorical
import numpy as np
import re


def _norm(x):
    x = x.replace("+", " " + ACCIDENTAL[0][0]).replace("-", " " + ACCIDENTAL[1][0])
    return x


class Quality:
    def __init__(self, quality):
        self._quality = quality

    def __str__(self):
        return self._quality
        
    @property
    def quality(self):
        return self._quality
    
    def _getComponents(self, quality, quality_name):
        quality = _norm(quality)
        match_tension = re.findall(r'\(.+?\)', quality)
        add_tension = []
        if match_tension:
            quality = re.sub('|'.join(match_tension), '', quality)
            try:
                add_tension = [c.strip() for c in match_tension[0].strip('()').split(",")]
            except ValueError:
                raise ValueError("Invalid Chord.")     

        priority = sorted(LABEL_CHORD_PRIORITY.items(), key=lambda x: x[1])
        tension = []
        altered_tension = []
        for k, v in priority:
            if quality.find(k) != -1:
                if v == 1:
                    altered_tension.append(k)
                else:
                    tension.append(k)
                
                quality = quality.replace(k, "")

        tension_value = [CHORD_VALUE.get(x) for x in tension]
        max_tension_value = sorted(tension_value, key=lambda x: x[0])[0][0]

        if all((quality_name != q) for q in [QUALITY_ADD, QUALITY_MINOR_ADD]):
            for v in CHORD_VALUE.values():
                if v[0] < max_tension_value:
                    if v[0] > 1:
                        tension.append(v[0])

        for k, v in priority:
            if k in add_tension:
                if v == 1:
                    altered_tension.append(k)
                else:
                    tension.append(k)

        tension = sorted(set(tension), key=lambda x: CHORD_VALUE.get(x)[0])

        return tension, altered_tension

    def _getQuality(self, quality):
        priority = sorted(CHORD_QUALITY.items(), key=lambda x: len(x[0]), reverse=True)
        quality_name = ""
        quality_value = (0, 0, 0, 0)
        for k, v in priority:
            if quality.find(k) != -1:
                quality_name = k
                quality_value = v
                quality = quality.replace(k, "")
        
        return quality_name, quality_value

    def _omit(self, quality_, values):
        values_ = values
        
        if quality_.find("omit") != -1:
            omit_ = quality_.split("omit")[-1].replace("(", "").replace(")", "")
            omit_num = list(omit_)

            omit_index = []
            for o in omit_num:
                if o == "1":
                    omit_index.append(values_[0])
                elif o == "3":
                    omit_index.append(values_[1])
                elif o == "5":
                    omit_index.append(values_[2])

            for idx in omit_index:
                values_.remove(idx)

        return values_
    
    def _convert(self, quality_):
        values = []

        quality_name, quality_value = self._getQuality(quality_)
        tension, altered_tension = self._getComponents(quality_, quality_name=quality_name)

        # 3和音を追加する
        values.extend([CHORD_root, CHORD_3rd, CHORD_5th])

        if LABEL_7th in tension:
            values.append(CHORD_VALUE.get(LABEL_7th)[1])
            tension.remove(LABEL_7th)
        
        for i in range(len(quality_value)):
            for j in reversed(range(len(values))):
                if values[j] == CHORD_QUALITY_MAJOR[i]:
                    values[j] = values[j] + quality_value[i]
                    break
        
        if altered_tension:
            for alt in altered_tension:
                add = 1 if ACCIDENTAL_SHARP in alt else -1
                alt_val = CHORD_VALUE.get(alt[1:])[1]
                values.append(alt_val + add)
                if alt_val in values:
                    values.remove(alt_val)
        
        if tension:
            for tens in tension:
                values.append(CHORD_VALUE.get(tens)[1])
        
        # SUSは3度の音を削除
        if quality_name == QUALITY_SUS:
            values.remove(CHORD_3rd)

        quality_value = np.array(quality_value)

        # 省略音
        values = self._omit(quality_, values)

        return np.array(values)

    def getNotes(self, root='C', on=None, categorical=False):
        
        values = self._convert(self._quality)
        
        key_number = note_to_value(root)

        values = (values + key_number) % 12

        if on is not None:
            key_number = note_to_value(on)
            values = np.insert(values, 0, key_number)

        _, idx = np.unique(values, return_index=True)
        values = values[np.sort(idx)]

        if categorical:
            values = to_categorical(values)

        return values
