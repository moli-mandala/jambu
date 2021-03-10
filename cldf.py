import json
import csv
import unidecode

superscript = {
    'a': 'ᵃ', 'e': 'ᵉ', 'i': 'ᶦ',
    'o': 'ᵒ', 'u': 'ᵘ', 'ü': 'ᵘ̈',
    'y': 'ʸ', 'ə': 'ᵊ', 'ŭ': 'ᵘ̆',
    'z': 'ᶻ', 'gy': 'ᵍʸ', 'h': 'ʰ',
    'ŕ': 'ʳ́', 'ĕ': 'ᵉ̆', 'n': 'ⁿ'
}

with open('data/all.json', 'r') as fin:
    data = json.load(fin)

with open('cldf/cognates.csv', 'w') as fout, open('cldf/parameters.csv', 'w') as fout2:
    write = csv.writer(fout)
    write2 = csv.writer(fout2)
    write.writerow(['Cognateset_ID', 'Language_ID', 'Form', 'Description', 'Source'])
    write2.writerow(['ID', 'Name', 'Concepticon_ID', 'Description'])
    for entry in data:
        headword = data[entry][0]
        write.writerow([entry, 'Indo-Aryan', headword['words'][0], '', ''])
        write2.writerow([entry, headword['words'][0], '', ''])

a = set()
with open('cldf/forms.csv', 'w') as fout:
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
                    write.writerow([num, lang, entry, word, '', '', '', entry, '', 'CDIAL'])
                else:
                    if word[0] == '': continue
                    for i in superscript:
                        word[0] = word[0].replace(f'<superscript>{i}</superscript>', superscript[i])
                    write.writerow([num, lang, entry, word[0], word[1], '', '', entry, '', 'CDIAL'])

print(sorted(list(a)))
b = set()
with open('cldf/languages.csv', 'r') as fin:
    for row in fin.readlines():
        x = row.split(',')[0]
        b.add(x)

for i in a:
    if i not in b:
        print(i)