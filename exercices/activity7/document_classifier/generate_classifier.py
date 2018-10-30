# encoding=utf-8

import os
import pickle
import random
import nltk
from nltk.corpus import stopwords

def load_sentilex():
    sentilex = dict()
    arq = open('sentilexpt.txt', 'r')
    lines = arq.read().split('\n')
    for line in lines:
        splited = line.split('.')
        attr = splited[1].split(';')
        pol = int(attr[2].split('=')[1])
        pos = attr[0].split('=')[1]
        sentilex[splited[0]] = {'pol': pol, 'pos': pos}

    return sentilex


def load_docs(path='corpus'):
    styles = ['funk', 'gospelreligioso']

    for style in styles:
        style_dir = os.path.join(path, style)
        for _, subdirs, files in os.walk(style_dir):
            for lyric_name in files[:500]:
                lyric_path = os.path.join(style_dir, lyric_name)
                lyric = open(lyric_path, 'r')
                yield lyric.read(), style
                lyric.close()

def get_features(doc):
    words = doc.split()
    num_words = len(words)
    docWords = set(words)
    words_size = 0
    positive_words = 0
    negative_words = 0
    not_found_words = 0
    classes = list()

    feats = {}
    for word in wFeats:
        words_size += len(word)
        if word in docWords:
            cont = u'contains({})'.format(word)
            if cont in feats:
                feats[cont] = feats[cont] + 1
            else:
                feats[cont] = 0
            if word in sentilex:
                if sentilex[word]['pol'] > 0:
                    positive_words = positive_words + 1
                if sentilex[word]['pol'] < 0:
                    negative_words = negative_words + 1
                classe = 'classe({})'.format(sentilex[word]['pos'])

                if classe in feats:
                    feats[classe] = feats[classe] + 1
                else:
                    classes.append(classe)
                    feats[classe] = 1

            else:
                not_found_words = not_found_words + 1

    for classe in classes:
        feats[classe] = feats[classe] / num_words

    feats['non-repeated-words-ration'] = num_words / len(docWords)
    feats['words-average-size'] = words_size/num_words
    feats['words-count'] = num_words
    feats['positive'] = positive_words
    feats['negative'] = negative_words
    feats['not-found-words'] = not_found_words

    return feats

sentilex = load_sentilex()
docs = [d for d in load_docs()]
words = set()
for doc in docs:
    text = doc[0].replace(',', ' ,').replace('.', ' .')
    text = text.replace('!', ' !').replace('?', ' ?')
    for word in text.split():
        words.add(word.lower())

allWords = nltk.FreqDist(words)
wFeats = list(allWords)

if __name__ == '__main__':
    fsets = [(get_features(d), c) for (d,c) in docs]
    trainSet, testSet = fsets[100:], fsets[:100]
    c1 = nltk.NaiveBayesClassifier.train(trainSet)
    print('Acurácia: '+str(nltk.classify.accuracy(c1, testSet)))

    f = open('classifier.pkl', 'wb')
    pickle.dump(c1, f)
    f.close()