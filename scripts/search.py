import json, os
import re

words = []
for file in sorted(os.listdir('output')):
    with open('output/' + file, 'r') as fin:
        data = json.load(fin)
        etymon = data[0]['words']
        tot = len(data) - 1
        if tot < 5: continue
        ct = 0
        if re.search('.[ṅnmñṇṁ]', etymon): continue
        for lang in data[1:]:
            # if lang['lang'] != 'Hind\u012b': continue
            for word in lang['words']:
                if '\u00e3' in word or '\u0303' in word or '\u02dc' in word:
                    # print(etymon, lang['lang'], word, sep=',')
                    ct += 1
                    break
        if ct > 0:
            words.append([ct / tot, etymon])

for i in sorted(words):
    print(i)