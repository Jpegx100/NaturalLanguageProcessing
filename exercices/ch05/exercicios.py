#####################################
#            Exercício 8            #
#####################################

e = {
    'word': 'chair',
    'part-of-speech': 'SUB',
    'sense': 'a type of seat',
    'example': 'She will seat on the chair'
}

#####################################
#            Exercício 9            #
#####################################

from nltk.text import Text
Text(brown.words()).concordance('go')
Text(brown.words()).concordance('went')

#>>> Ambas as palavras aparecem após substantivos ou pronomes. A palavra
#>>> 'go' aparece costumeiramente depois 'to', 'would', 'will', 'may' já
#>>> a palavra 'went' não aparece depois destas palavras.

#####################################
#            Exercício 13           #
#####################################

date = {
    'D': '09',
    'M': 'August',
    'm': '08',
    'Y': '1995',
    'y': '95'
}
print '{D} of {M}, {Y}.'.format(**date)
print '{D}/{m}/{y}'.format(**date)


#####################################
#            Exercício 14           #
#####################################
from nltk.corpus import brown

tags = []
for sent in brown.tagged_sents():
    for (word, tag) in sent:
        tags.append(tag)

sorted(set(tags))
