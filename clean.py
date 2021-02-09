import json
from collections import Counter

data = {}

indological_mapping = [
    '~', 'a', 'aː', 'i', 'iː', 'u', 'uː', 'e', 'eː', 'o', 'oː',
    'k', 'kʰ', 'g', 'gʱ', 'ŋ',
    ''
]

counts = Counter()

with open('cdial_stripped.csv', 'r') as fin:
    for line in fin:
        row = line.strip().split('\t')
        if row[0] not in data:
            data[row[0]] = []
        row[1] = row[1].strip('# ')
        row[2] = row[2].strip('# ')
        counts[row[2]] += 1
        data[row[0]].append({
            'term': row[1],
            'etym': [
                {'term': row[2], 'source': 'cdial'}
            ],
            'source': 'cdial'
        })

print(counts.most_common(20))

for lang in data:
    with open(f'data/{lang}.csv', 'w') as fout:
        data[lang].sort(key=lambda x: x['term'])
        json.dump(data[lang], fout, indent=2, ensure_ascii=False)