import csv
import lingpy
from collections import Counter

forms = {}
with open('cldf/forms.csv') as fin:
    reader = csv.reader(fin)
    for i, row in enumerate(reader):
        if i == 0: continue
        if row[1] not in ['Indo-Aryan', 'S']: continue
        if row[2] not in forms: forms[row[2]] = []
        forms[row[2]].append([row[1], row[3].strip('-, *')])

cts = Counter()
with open('test.out', 'a') as fout:
    for i in forms:
        if len(forms[i]) == 1: continue
        forms[i].sort()
        try:
            m = lingpy.Multiple([x[1] for x in forms[i]])
            m.prog_align()
            strs = [['#'] + list(x.split()) + ['#'] for x in str(m).split('\n')]
            l = len(strs[0])
            for i in range(l):
                for reflex in strs:
                    if reflex[i] == 'b':
                        l, r = i - 1, i + 1
                        while strs[0][l] == '-':
                            l -= 1
                        while strs[0][r] == '-':
                            r += 1
                        
                        k = f'{strs[0][l]}_{strs[0][i]}_{strs[0][r]}'.replace(' ', '')
                        cts[k] += 1
        except:
            continue

    for value, count in cts.most_common():
        fout.write(f'{value} {count}\n')