# encoding=utf-8

import os
import pickle
import random
import nltk
from nltk.corpus import stopwords


def load_docs(path='corpus'):
    styles = [x for x in os.listdir(path)]

    for style in styles:
        style_dir = os.path.join(path, style)
        for _, subdirs, files in os.walk(style_dir):
            for lyric_name in files:
                lyric_path = os.path.join(style_dir, lyric_name)
                lyric = open(lyric_path, 'r')
                yield lyric.read(), style
                lyric.close()

def get_features(doc, postagger):
    docWords = set(doc)
    tam = len(docWords)

    feats = {}
    for word in wFeats:
        feats[u'contains({})'.format(word)] = (word in docWords)
        classe = postagger.classify({'text': word})
        if classe in feats:
            feats[classe] = feats[classe] + 1
        else:
            feats[classe] = 1

    feats['tam'] = tam
    return feats

stopwords = stopwords.words('portuguese')
docs = [d for d in load_docs()]
words = set()
for doc in docs:
    for word in doc[0].split():
        if word.lower() not in stopwords:
            words.add(word.lower())

allWords = nltk.FreqDist(words)
wFeats = list(allWords)[:2000]

if __name__ == '__main__':
    postagger = pickle.load(open('postagger.pickle', 'rb'))
    fsets = [(get_features(d, postagger), c) for (d,c) in docs]
    trainSet, testSet = fsets[100:], fsets[:100]
    c1 = nltk.NaiveBayesClassifier.train(trainSet)
    print('Acurácia: '+str(nltk.classify.accuracy(c1, testSet)))

    f = open('classifier.pkl', 'wb')
    pickle.dump(c1, f)
    f.close()