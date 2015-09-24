import nltk
import random
from nltk.corpus import names

def caract(w):
    letramaisrepetida = ''
    vezes = 0
    for l in w:
        if w.count(l) > vezes:
            letramaisrepetida = l
            vezes = w.count(l)
    return {'ultima_letra':w[-1],
            'letra_mais_repetida':letramaisrepetida}

def cl_random_name():
    w = random.choice(nome_etq)
    result = classificador.classify(caract(w))
    n, g = w
    print(n+'('+g+') is '+str(result))

nome_etq = [(name, 'male') for name in names.words('male.txt')]+[(name, 'female') for name in names.words('female.txt')]
random.shuffle(nome_etq)
caracts = [(caract(nome), genero) for (nome, genero) in nome_etq]
conjunto_treino = caracts[int(len(caracts)/2):]
conjunto_teste = caracts[:int(len(caracts)/2)]
classificador = nltk.NaiveBayesClassifier.train(conjunto_treino)

print("Acuracia com conjunto de teste: "+str(nltk.classify.accuracy(classificador, conjunto_teste)))
print("Acuracia com conjunto de treino: "+str(nltk.classify.accuracy(classificador, conjunto_treino)))
