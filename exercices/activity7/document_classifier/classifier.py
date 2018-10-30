# encoding=utf-8

import sys
import nltk
import pickle
from generate_classifier import get_features

if __name__ == '__main__':

    if len(sys.argv) > 1:
        classifier = pickle.load(open('classifier.pkl', 'rb'))

        arq = open(sys.argv[1], 'r')
        input_text = arq.read()
        classe = classifier.classify(get_features(input_text))
        print(classe)

    else:
        print('Você deve passar o arquivo de entrada')
