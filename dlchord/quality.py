from .const import CHORD_COMP_PRIORITY, TENSION
from .const import CHORD_QUALITY, CHORD_QUALITY_MAJOR
from .const import ACCIDENTAL, ACCIDENTAL_VAL
from .const import QUALITY_SUS, QUALITY_ADD, QUALITY_MINOR_ADD
from .const import CHORD_VALUE
from .const import CHORD_root, CHORD_3rd, CHORD_5th
from .const import SCALE_FLAT, SCALE_SHARP
import numpy as np


def _norm(x):
    x = x.replace("+", " " + ACCIDENTAL[0][0]).replace("-", " " + ACCIDENTAL[1][0])
    return x


def to_categorical(x, classes=12):
    y = np.zeros((classes))
    y[x[0] - 1] = 2
    for i in range(1, len(x)):
        y[x[i] - 1] = 1

    return y


def keynumber(key):
    if key == '' or key is None:
        raise ValueError("Input value is invalid")

    # key = _norm(key)

    if any((s in key) for s in ACCIDENTAL[0]):
        scale_number = SCALE_SHARP
    elif any((s in key) for s in ACCIDENTAL[1]):
        scale_number = SCALE_FLAT
    else:
        scale_number = SCALE_FLAT

    if len(key) > 2:
        result_num = scale_number.index(key[:1]) + ACCIDENTAL_VAL[key[1]] + ACCIDENTAL_VAL[key[2]]
    elif len(key) > 1:
        result_num = scale_number.index(key[:1]) + ACCIDENTAL_VAL[key[1]]
    else:
        result_num = scale_number.index(key)
    
    result_num = result_num % len(SCALE_FLAT)

    return result_num


class Quality:
    def __init__(self, quality):
        self._quality = quality

    def __str__(self):
        return self._quality
        
    @property
    def quality(self):
        return self._quality
    
    def _getComponent(self, quality):
        quality = _norm(quality)
        priority = sorted(CHORD_COMP_PRIORITY.items(), key=lambda x: x[1])
        chord_comp = []
        tension = []
        for k, v in priority:
            if quality.find(k) != -1:
                if k in TENSION:
                    tension.append(k)
                else:
                    chord_comp.append(k)
                
                quality = quality.replace(k, "")

        return chord_comp, tension

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

        chord_component, tension = self._getComponent(quality_)
        quality_name, quality_value = self._getQuality(quality_)

        # 3和音を追加する
        values.extend([CHORD_root, CHORD_3rd, CHORD_5th])

        # 構成音を追加する
        values.extend([CHORD_VALUE[v][1] for v in chord_component])

        # テンションを追加する
        if len(tension) >= 1:
            comp_add = []
            comp_alt = []
            for x in tension:
                if CHORD_VALUE.get(x) is not None:
                    comp_add.append((CHORD_VALUE.get(x)[0], CHORD_VALUE.get(x)[1]))
                else:
                    add = 1 if x[0] in ACCIDENTAL[0] else -1
                    comp_alt.append((CHORD_VALUE.get(x[1:])[1], add))

            if len(comp_add) >= 1:
                comp_add = sorted(comp_add, key=lambda x: x[0])
                if all((quality_name != q) for q in [QUALITY_ADD, QUALITY_MINOR_ADD]):
                    for v in CHORD_VALUE.values():
                        if v[0] < comp_add[0][0] and v[0] > 1:
                            values.append(v[1])
                    for v in comp_add:
                        values.append(v[1])
                else:
                    for v in comp_add:
                        values.append(v[1])

            values.extend([v[0] + v[1] for v in comp_alt])
            for v in comp_alt:
                if v[0] in values:
                    values.remove(v[0])
        
        # SUSは3度の音を削除
        if quality_name == QUALITY_SUS:
            values.remove(CHORD_3rd)

        quality_value = np.array(quality_value)

        # 省略音
        values = self._omit(quality_, values)

        for i in range(len(quality_value)):
            for j in range(len(values)):
                if values[j] == CHORD_QUALITY_MAJOR[i]:
                    values[j] = values[j] + quality_value[i]

        return np.array(values)

    def getNotes(self, root='C', on=None, norm=False, categorical=False):
        
        values = self._convert(self._quality)
        
        key_number = keynumber(root)

        values = (values + key_number) % 12
        values = np.where(values == 0, 12, values)

        if on is not None:
            key_number = keynumber(on)
            values = np.insert(values, 0, key_number + 1)

        _, idx = np.unique(values, return_index=True)
        values = values[np.sort(idx)]

        if categorical:
            values = to_categorical(values)

        if norm:
            values = values / np.max(values)

        return values
