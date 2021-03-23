from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import csv
import re

chars = ['p', 'b', 'bAsp', 'f', 'v', 'w', 'm', 'uFrn', 'u', 'o', 'oFrn', 'uTns', 'oTns',
         'cDen', 'zDen', 't', 'd', 'dAsp', 's', 'z', 'l', 'lVls', 'n', 'cRet', 'jRet',
         'tRet', 'dRet', 'dRetAsp', 'sRet', 'zRet', 'r', 'rFlp', 'lBak', 'rApx', 'nApx',
         'nRet', 'rVoc', 'cLam', 'jLam', 'jLamAsp', 'sLam', 'zLam', 'y', 'i', 'e', 'aLam',
         'iTns', 'eTns', 'kPal', 'gPal', 'gPalAsp', 'k', 'g', 'gAsp', 'x', 'gSpi', 'nasVel',
         'iBak', 'a', 'aOpn', 'aRnd', 'kLab', 'gLab', 'gLabAsp', 'nas', 'q', 'hPhyr', 'Ayn',
         'AgltStp', 'h', 'hPglt', 'hPgltRnd']

languages = ['IndoAryan/Pashai/Degan/DeganLanguage',
             'Nuristani/Kamkata/Kom/KomLanguage',
             'Nuristani/Kamkata/Kata/KataLanguage',
             'Nuristani/AshkunEtc/SaNu/SaNuLanguage',
             'Nuristani/Kalasha/Nishei/NisheiLanguage',
             'IndoAryan/Chitral/Khow/KhowLanguage',
             'IndoAryan/Indus/Atsaret/AtsaretLanguage']

codes = ['deg', 'Kam', 'Kata', 'Ash', 'Wg', 'Kho', 'Phal']

with open('strand.csv', 'w') as fout:
    writer = csv.writer(fout)
    for i, language in enumerate(languages):
        for char in chars:
            link = f'http://nuristan.info/{language}/Lexicon/alph-{char}.html'
            print(link)
            try:
                with urlopen(Request(link, headers={'User-Agent': 'Mozilla/5.0'})) as resp:
                    soup = BeautifulSoup(resp, 'html.parser')
                    for data in soup.find_all(class_='dic'):
                        word = data.find(class_='l')
                        if word:
                            word = word.find(text=True, recursive=False)
                            l = re.search(r'<b>]</b>\xa0 (.*?)\.\xa0 (.*?)\.', str(data))
                            if not l:
                                l = re.search(r'</span>\xa0 (.*?)\.\xa0 (.*?)\.', str(data))
                            if l:
                                pos = l.group(1).lower()
                                definition = l.group(2).lower()
                                turner = re.search(r'T\. (\d+)', str(data))
                                if turner:
                                    turner = turner.group(1)
                                    writer.writerow([codes[i], turner, word, definition, '', '', '', 'strand'])

            except HTTPError as e:
                pass