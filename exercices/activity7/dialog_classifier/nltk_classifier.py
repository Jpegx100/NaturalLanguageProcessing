import nltk
import pickle

def remove_stop_words(sentence):
    stop_words = nltk.corpus.stopwords.words('portuguese')
    sent = sentence
    for sw in stop_words:
        sent = sent.replace(sw, '')
    return sent

def get_data(dataset_path='conversas.txt'):
    results = list()

    arq = open(dataset_path, 'r')
    raw = arq.read().lower()

    lines = raw.split('\n')
    for line in lines:
        splited_line = line.split(',')
        sentence = ','.join(splited_line[:-2])
        results.append(
            (remove_stop_words(sentence), int(splited_line[-2]))
        )

    return results

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

dataset = get_data()
fSets = [(get_features(text, postagger), label) for (text, label) in dataset]
size = int(len(fSets) * 0.1)
trainSet, testSet = fSets[size:], fSets[:size]
c1 = nltk.NaiveBayesClassifier.train(trainSet)
print(nltk.classify.accuracy(c1, testSet))

f = open('classifier.pickle', 'wb')
pickle.dump(c1, f)
f.close()
