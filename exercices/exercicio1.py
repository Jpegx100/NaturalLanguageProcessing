# 4

len(text2)
len(set(text2))

#6
# >>> Elinor e Marianne são provavelmente os de protagonistas do texto.

# 7
text5.collocations()

# 9
string = 'Hello world'
string
print(string)
print(var_string + var_string)
print(var_string*2)
print(' '.join([var_string, var_string]))


# 10
my_sent = ["Fulano", "de", "Tal"]

# 15
sorted(w for w in text5 if w.startswith('b'))

# 19
sorted(set(w.lower() for w in text1))
sorted(w.lower() for w in set(text1))

# 22

print([w for w in text5 if len(w) == 4])
print(frequencia = FreqDist(text5))
print([frequencia[w] for w in text5 if len(w) == 4])

# 24

print([w for w in text6 if w.endswith('ize')])
print([w for w in text6 if 'z' in w])
print([w for w in text6 if 'pt' in w])
print([w for w in text6 if w.istitle()])

# 25

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
print([w for w in sent if w.startswith('sh')])
print([w for w in sent if len(w) > 4])

# 26
def soma(text1):
    return sum(len(w) for w in text1) / len(text1)

# 27
def tamanhoVocabulario(text):
	return len(set(text))


# 28
def porcentagem(palavra, text):
	return 100 * (text.count(palavra) / len(text))