import wget
import os


path = 'result'

if not os.path.exists(path):
    os.makedirs(path)

type = [
    'arabic',
    'bengaliP',
    'bengaliT',
    'englishP',
    'englishT',
]

for sura in range(1, 115):
    for ayat in range(1, 290):
        file = 'http://quran.gov.bd/quran/{}/{}/{}-{}.png'.format(type[2], sura, sura, ayat)

        try:
            wget.download(file, out=path)
        except:
            print(ayat)
            break
