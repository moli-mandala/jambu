import csv
import lingpy
from collections import defaultdict

forms = defaultdict(list)
with open('cldf/forms.csv') as fin:
    reader = csv.reader(fin)
    for i, row in enumerate(reader):
        if i == 0: continue
        forms[row[2]].append([row[1], row[3].strip('-, *')])

name = {}
with open('cldf/languages.csv') as fin:
    reader = csv.reader(fin)
    for i, row in enumerate(reader):
        if i == 0: continue
        name[row[0]] = row[1]

res = defaultdict(lambda: defaultdict(int))
with open('test.out', 'a') as fout:
    for _, form in enumerate(forms):
        print(_)
        if 'kṣ' not in forms[form][0][1]: continue
        try:
            if len(forms[form]) == 1: continue
            # forms[i].sort()
            m = lingpy.Multiple([x[1] for x in forms[form]])
            m.prog_align()
            strs = [['#'] + list(x.split()) + ['#'] for x in str(m).split('\n')]
            print(strs)
            
            l, r = -1, -1
            for i in range(len(strs[0])):
                if strs[0][i] == 'k':
                    l = i
                    for j in range(i + 1, len(strs[0])):
                        if strs[0][j] == 'ṣ':
                            r = j
                            break
                        elif strs[0][j] != '-':
                            l = -1
                            r = -1
                            break
                    break
            
            for _, lang in enumerate(strs):
                reflex = (''.join(lang[l:r + 1])).replace('-', '')
                res[forms[form][_][0]][reflex] += 1
        except:
            pass
        
for lang in res:
    tot = sum([res[lang][outcome] for outcome in res[lang]])
    print(name[lang], (res[lang]['kh'] + res[lang]['kkh'] + res[lang]['k']) / tot, tot, sep=',')