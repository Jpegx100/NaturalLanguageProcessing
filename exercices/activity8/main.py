import nltk
from nltk.corpus import names
import random


################# Questão 2 #################
print('>>> Questão 2 >>>')

names = (
    [(name, 'male') for name in names.words('male.txt')] +
    [(name, 'female') for name in names.words('female.txt')]
)
random.shuffle(names)
test, devtest, training = names[:500], names[500:1000], names[1000:]

def gender_features(name):
    nlower = name.lower()
    feats = {
        "firstletter": nlower[0],
        "lastletter": nlower[-1],
        "suffix2": nlower[-2:],
        "suffix3": nlower[-3:],
        "prefix3": nlower[:3],
    }
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        feats["count(%s)" % letter] = name.lower().count(letter)
        feats["has(%s)" % letter] = (letter in name.lower())
    return feats

train_set = [(gender_features(n), g) for (n,g) in training]
devtest_set = [(gender_features(n), g) for (n,g) in devtest]

classifier_nv = nltk.NaiveBayesClassifier.train(train_set)
acuracia = nltk.classify.accuracy(classifier_nv, devtest_set)
print("Acuracia NaiveBayes: "+str(acuracia))

################# Questão 5 #################
# Utilizei o mesmo classificador da questão dois
print('>>> Questão 5 >>>')

classifier_dt = nltk.DecisionTreeClassifier.train(train_set)
acuracia = nltk.classify.accuracy(classifier_dt, devtest_set)
print("Acuracia DecisionTree: "+str(acuracia))

classifier_me = nltk.MaxentClassifier.train(train_set, max_iter=20)
acuracia = nltk.classify.accuracy(classifier_me, devtest_set)
print("Acuracia MaxEnt: "+str(acuracia))

################# Questão 4 #################
print('>>> Questão 4 >>>')

from nltk.corpus import movie_reviews
docs = [
    (list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)
]

words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(words.keys())[:2000]
def get_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

featuresets = [(get_features(d), c) for (d,c) in docs]
train_set, test_set = featuresets[100:], featuresets[:100]
c1 = nltk.NaiveBayesClassifier.train(train_set)

acuracia = nltk.classify.accuracy(c1, test_set)
print("Acuracia: "+str(acuracia))
