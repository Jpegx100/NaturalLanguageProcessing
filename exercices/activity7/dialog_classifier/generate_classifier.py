# encoding=utf-8
import nltk
import pickle

def remove_stop_words(sentence):
    stop_words = nltk.corpus.stopwords.words('portuguese')
    sent = sentence
    for sw in stop_words:
        sent = sent.replace(sw, '')
    return sent

def get_data(dataset_path='corpus.txt'):
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

if __name__ == '__main__':

    postagger_file = open('postagger.pickle', 'rb')
    postagger = pickle.load(postagger_file)
    postagger_file.close()

    dataset = get_data()
    fSets = [(get_features(text, postagger), label) for (text, label) in dataset]
    size = int(len(fSets) * 0.1)
    trainSet, testSet = fSets[size:], fSets[:size]
    c1 = nltk.NaiveBayesClassifier.train(trainSet)
    print('Acurácia: '+str(nltk.classify.accuracy(c1, testSet)))

    f = open('classifier.pkl', 'wb')
    pickle.dump(c1, f)
    f.close()
