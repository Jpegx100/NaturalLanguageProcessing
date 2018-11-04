import nltk
from nltk.corpus import mac_morpho


def pFeatures(tokens, i):
    if i > 0 and tokens[i-1]:
        prev_word_cap = tokens[i-1][0].isupper()
    else:
        prev_word_cap = False

    return {
        'next-word-capitalized': tokens[i+1][0].isupper(),
        'prev-word-capitalized': prev_word_cap,
        'prev-word': tokens[i-1].lower(),
        'punct': tokens[i],
    }

sents = mac_morpho.sents()
tokens = list()
limites = set()
offset = 0
for s in sents:
    tokens.extend(s)
    offset += len(s)
    limites.add(offset-1)

fsets = [
    (pFeatures(tokens, i), (i in limites))
    for i in range(1, len(tokens)-1) if tokens[i] in '.?!'
]

size = int(len(fsets) * 0.1)
trainSet, testSet = fsets[size:], fsets[:size]
c1 = nltk.NaiveBayesClassifier.train(trainSet)
acuracia = nltk.classify.accuracy(c1, testSet)
print("Acurácia: "+str(acuracia))