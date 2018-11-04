import numpy as np
import tensorflow as tf
from tensorflow import keras
from random import shuffle

class TensorFlowClassifier(object):
    raw = None
    texts = list()
    labels = list()
    non_stop_words = set()
    sentences = list()
    stop_words = list()
    word2int = dict()
    int2word = dict()

    def __init__(self, dataset_path='conversas.txt'):

        with open(dataset_path, 'r') as arq:
            self.raw = arq.read().lower()

        lines = self.raw.split('\n')
        for line in lines:
            splited_line = line.split(',')
            sentence = ','.join(splited_line[:-2])
            self.labels.append(int(splited_line[-2]))
            self.sentences.append(sentence)

        stop_words = self.load_stop_words()
        sentences_nsw = [
            self.remove_stop_words(sentence) for sentence in self.sentences
        ]

        self.non_stop_words = set(' '.join(sentences_nsw).split())
        for i, word in enumerate(self.non_stop_words):
            self.word2int[word] = i
            self.int2word[i] = word

        for sent_ns in sentences_nsw:
            self.texts.append([self.word2int[word] for word in sent_ns.split()])

    def get_data(self):
        return self.texts, self.labels

    def load_stop_words(self):
        return ['.', '?', '!', ':']

    def remove_stop_words(self, sentence):
        sent = sentence.replace(',', '')
        for sw in self.stop_words:
            sent = sent.replace(sw, '')
        return sent


tsc = TensorFlowClassifier()
texts, labels = tsc.get_data()

limit = 50
(test_data, test_labels) = (texts[:limit], labels[:limit])
(train_data, train_labels) = (texts[limit:], labels[limit:])

train_data = keras.preprocessing.sequence.pad_sequences(
    train_data, value=0, padding='post', maxlen=50
)
test_data = keras.preprocessing.sequence.pad_sequences(
    test_data, value=0, padding='post', maxlen=50
)


vocab_size = len(tsc.non_stop_words)

model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation=tf.nn.relu))
model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

model.compile(
    optimizer=tf.train.AdamOptimizer(),
    loss='binary_crossentropy',
    metrics=['accuracy']
)


limit_train = 50
partial_x_train = train_data[limit_train:]
partial_y_train = train_labels[limit_train:]

# test do treinamento
x_val = train_data[:limit_train]
y_val = train_labels[:limit_train]

history = model.fit(
    # partial_x_train,
    # partial_y_train,
    train_data,
    train_labels,
    epochs=100,
    # validation_data=(x_val, y_val)
)
a, b = model.evaluate(test_data, test_labels)
print(a)
print(b)

pre = model.predict(test_data)
import pdb;pdb.set_trace()