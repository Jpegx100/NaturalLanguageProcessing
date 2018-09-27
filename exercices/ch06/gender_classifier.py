import random
import nltk

def gender_features(word):
    word_lower = word.lower()

    most_repeated_letter = ''
    repeating_count = 0
    for l in word_lower:
        if word_lower.count(l) > repeating_count:
            most_repeated_letter = l
            repeating_count = word_lower.count(l)

    features = {
        'as': word_lower.count('a'),
        'sufixo1': word_lower[-1],
        'sufixo2': word_lower[-2:],
        'sufixo3': word_lower[-3:],
        'most_repeated_letter': most_repeated_letter
    }

    return features

def load_names():
    mal = open('masc.txt', 'r')
    fem = open('femi.txt', 'r')
    male_names = mal.read().split('\n')
    female_names = fem.read().split('\n')
    return male_names, female_names

if __name__ == '__main__':
    male_names, female_names = load_names()

    names = (
        [(name, 'masculino') for name in male_names] +
        [(name, 'feminino') for name in female_names]
    )
    random.shuffle(names)

    featuresets = [(gender_features(n), gender) for (n, gender) in names]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(5)
