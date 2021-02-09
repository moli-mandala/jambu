import json, os

with open('index.json', 'w') as fout:
    json.dump(sorted(os.listdir(path='.')), fout, indent=2)