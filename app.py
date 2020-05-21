import wget
import os


path = 'asset/audio/a'

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
        file = 'http://quran.gov.bd/quran/{}/{}/{}-{}.mp3'.format(type[0], sura, sura, ayat)

        try:
            wget.download(file, out=path)
        except:
            break
