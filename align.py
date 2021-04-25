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
        forms[row[2]].append([row[1], row[6].strip('-, *')])

cts = Counter()
with open('test.out', 'a') as fout:
    for i in forms:
        if len(forms[i]) == 1: continue
        try:
            forms[i].sort()
            m = lingpy.Multiple([x[1] for x in forms[i]])
            m.prog_align()
            strs = [['#'] + list(x.split()) + ['#'] for x in str(m).split('\n')]
            l = len(strs[0])
            for char in range(l):
                for j, reflex in enumerate(strs):
                    if forms[i][j] != 'Indo-Aryan':
                        if 'd͡ʒ' == reflex[char]:
                            l, r = char - 1, char + 1
                            while strs[0][l] == '-':
                                l -= 1
                            while strs[0][r] == '-':
                                r += 1
                            
                            k = f'{strs[0][l]}_{strs[0][char]}_{strs[0][r]} > {reflex[char]}'.replace(' ', '')
                            cts[k] += 1
        except:
            continue

    for value, count in cts.most_common():
        fout.write(f'{value} {count}\n')