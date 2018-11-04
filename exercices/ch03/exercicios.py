#####################################
############# Questão 1 #############
#####################################

def stem(pal):
    sufixos = [
        'dade', 'ez', 'eza', 'ança', 'ismo', 'dor',
        'nte', 'ada', 'gem', 'ria', 'ado', 'ada'
    ]

    for sufixo in sufixos:
        if pal.endswith(sufixo):
            return pal[:-len(sufixo)]
    return pal

#####################################
############# Questão 2 #############
#####################################

#####################################
#            Exercício 8            #
#####################################
print('Monty' < 'Python')
print('Z' < 'a')
print('z' < 'a')
print('Monty' < 'Montague')
print(('Monty', 1) < ('Monty', 2))
print(('Monty', 1) < ('Montague', 2))
print((1, 'Monty') < (2, 'Montague'))

#####################################
#            Exercício 9            #
#####################################
# a)
texto = '  text    whit whitespace  '
print(' '.join(texto.split()))
# b)
import re
novo_texto = re.sub(r'\s+', ' ', re.sub(r'^\s+|\s+$', '', texto))
print(novo_texto)

#####################################
#            Excrcício 13           #
#####################################
palavra_vogais = [[]]
palavras = ['O', 'cachorro', 'trouxe', 'o', 'jornal']
for palavara in palavras:
    if (len(palavara) > len(palavra_vogais)-1):
        for index in range(len(palavra_vogais), len(palavara)+1):
            palavra_vogais.append([])
    num_vowels = len(re.findall(r'[aeiouAEIOU]', palavara))
    if (num_vowels > len(palavra_vogais[len(palavara)])-1):
        for index in range(len(palavra_vogais[len(palavara)]), num_vowels+1):
            palavra_vogais[len(palavara)].append(set())
    palavra_vogais[len(palavara)][num_vowels].add(palavara)
print palavra_vogais[3][1]
print palavra_vogais[9][3]

#####################################
#            Excrcício 14           #
#####################################
from nltk.book import *

def novel10(text):
    texto_dividido = len(text) / 10
    palavras = []
    for palavra in text[-texto_dividido:]:
        if palavra not in text[:-texto_dividido]:
            palavras.append(palavra)

    return palavras

#####################################
#            Excrcício 18           #
#####################################

def see_words(prop, value):
    lex = [
        ('cadeira', 'móvel usado para sentar-se', 'ca-de-i-ra'),
        ('carro', 'veículo usado para locomoção', 'ca-rro'),
        ('piano', 'instrumento musical', 'pi-a-no'),
        ('camisa', 'peça de roupa', 'ca-mi-sa'),
    ]

    if prop == 'meaning':
        return [w for (w, m, p) in lex if m == value]
    if prop == 'pronunciation':
        return [w for (w, m, p) in lex if p == value]

print(see_words('camisa', 'ca-mi-sa'))

#####################################
#            Excrcício 20           #
#####################################
import nltk

def sort_words(words):
    fdist = nltk.FreqDist(words)
    return fdist.keys()

words = ['banana', 'banana', 'queijo', 'banana',
'queijo', 'queijo', 'maça', 'maça', 'queijo']
print(sort_words(words))

#####################################
#            Excrcício 21           #
#####################################

def words_not_in_vocalubare(text, vocab):
    words = set(text).difference(set(vocab))
    return words

uk_words = words_not_in_vocalubare(
    'Texty unkknown workds',
    nltk.corpus.words.words()
)

print(uk_words)

#####################################
#            Excrcício 30           #
#####################################
