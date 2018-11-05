# encoding=utf-8

import sys
import pickle
from generate_classifier import get_features

if __name__ == '__main__':

    if len(sys.argv) > 1:

        classifier = pickle.load(open('classifier.pkl', 'rb'))

        arq = open(sys.argv[1], 'r')
        input_text = arq.read().replace('.', ' .').replace('?', ' ?')
        input_text = input_text.replace('!', ' !').split()

        text = input_text[0]

        for i in range(1, len(input_text)-1):
            seg = ' '+input_text[i]
            if input_text[i] in '.?!':
                classe = classifier.classify(get_features(input_text, i))
                seg = ' <SEGMENTADOR>{}</SEGMENTADOR>' if classe else '{}'
                seg = seg.format(input_text[i])
            text += seg

        print(text)

    else:
        print('Você deve passar o arquivo de entrada')
