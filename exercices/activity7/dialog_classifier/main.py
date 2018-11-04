import nltk
import pickle

def get_features(post, postagger):
    features = {}
    classes = []
    words = nltk.word_tokenize(post)
    for word in words:
        classe = postagger.classify({'text': word})
        features['contains({})'.format(word.lower())] = True
        classes.append(classe)
    features['pattern'] = ' '.join(classes)
    return features

postagger = pickle.load(open('postagger.pickle', 'rb'))
classifier = pickle.load(open('classifier.pickle', 'rb'))
input_text = ''

while input_text != 'exit':
    input_text = input('Entre com o texto: ')
    print(classifier.classify(get_features(input_text, postagger)))