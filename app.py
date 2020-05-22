import wget
import os


path = 'asset/audio/et'

if not os.path.exists(path):
    os.makedirs(path)

result = open('result.txt', 'a')


def check(array, length, sura):
    if len(array) != length:
        result.write(sura + str(sorted(set(range(array[0], array[-1])) - set(array))) + '\n')


type = [
    'arabic',
    'bengaliP',
    'bengaliT',
    'englishP',
    'englishT',
]


for sura in range(10, 115):
    count = []
    for ayat in range(1, 290):
        file = 'http://quran.gov.bd/quran/{}/{}/{}/{}-{}.mp3'.format('Sound', 'english', sura, sura, ayat)

        try:
            wget.download(file, out=path)
            count.append(ayat)
        except:
            check(count, ayat - 1, sura)
            count = []
            break
