import nltk
nltk.corpus
from nltk.corpus import names

cfd = nltk.ConditionalFreqDist(
    (genre, name[0])
    for genre in names.fileids()
    for name in names.words(genre))
cfd.plot()
