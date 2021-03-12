import json
import csv
import unidecode
import re

superscript = {
    'a': 'ᵃ', 'e': 'ᵉ', 'i': 'ᶦ',
    'o': 'ᵒ', 'u': 'ᵘ', 'ü': 'ᵘ̈',
    'y': 'ʸ', 'ə': 'ᵊ', 'ŭ': 'ᵘ̆',
    'z': 'ᶻ', 'gy': 'ᵍʸ', 'h': 'ʰ',
    'ŕ': 'ʳ́', 'ĕ': 'ᵉ̆', 'n': 'ⁿ'
}

with open('data/all.json', 'r') as fin:
    data = json.load(fin)

with open('cldf/cognates.csv', 'w') as fout, open('cldf/parameters.csv', 'w') as fout2, open('data/extensions_ia.csv', 'r') as fin:
    write = csv.writer(fout)
    write2 = csv.writer(fout2)
    read = csv.reader(fin)
    write.writerow(['Cognateset_ID', 'Language_ID', 'Form', 'Description', 'Source'])
    write2.writerow(['ID', 'Name', 'Concepticon_ID', 'Description'])
    for entry in data:
        headword = data[entry][0]['words'][0].replace('ˊ', '́').replace(' --', '-').replace('-- ', '-')
        write.writerow([entry, 'Indo-Aryan', headword, data[entry][0]['ref'], 'cdial'])
        write2.writerow([entry, headword, '', data[entry][0]['ref']])
    for row in read:
        write.writerow(row)
        write2.writerow([row[0], row[2], row[3], row[4]])

a = set()
with open('cldf/forms.csv', 'w') as fout, open('data/extensions.csv', 'r') as fin:
    num = 0
    write = csv.writer(fout)
    write.writerow(['ID', 'Language_ID', 'Parameter_ID', 'Form', 'Gloss', 'Native', 'Phonemic', 'Cognateset', 'Description', 'Source'])
    for entry in data:
        headword = data[entry][0]
        for form in data[entry]:
            lang = form['lang'].replace('.', '')
            if lang == 'khaś': lang = 'khash'
            if lang == 'Māl': lang = 'Malw'

            lang = unidecode.unidecode(lang)
            a.add(lang)
            for word in form['words']:
                num += 1
                if lang == 'Indo-Aryan':
                    if word == '': continue
                    diffs = re.search(r'ʻ(.*?)ʼ', form['ref'])
                    desc = ''
                    if diffs != None:
                        desc = diffs.groups(2)[0].strip()
                    word = word.replace('ˊ', '́').replace(' --', '-').replace('-- ', '-')
                    write.writerow([num, lang, entry, word, desc, '', '', entry, '', 'CDIAL'])
                else:
                    if word[0] == '': continue
                    for i in superscript:
                        word[0] = word[0].replace('ˊ', '́').replace(' --', '-').replace('-- ', '-')
                        word[0] = word[0].replace(f'<superscript>{i}</superscript>', superscript[i])
                    write.writerow([num, lang, entry, word[0], word[1], '', '', entry, '', 'CDIAL'])
    
    read = csv.reader(fin)
    for i, row in enumerate(read):
        if i == 0: continue
        write.writerow([f'e{i}', row[0], row[1], row[2], row[3], row[4], row[5], row[1], row[6], row[7]])

print(sorted(list(a)))
b = set()
with open('cldf/languages.csv', 'r') as fin:
    for row in fin.readlines():
        x = row.split(',')[0]
        b.add(x)

for i in a:
    if i not in b:
        print(i)