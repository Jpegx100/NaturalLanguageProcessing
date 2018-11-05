import nltk

################# Questão 2 #################

# Padrão para frases nominais no singular: <DT>?<JJ.*>*<NN.*>+
# Padrão para frases nominais no plural: <DT>?<JJ.*>*<NN.*>*<NNS>+

################# Questão 3 #################
print('>>> Questão 3 >>>')

from nltk.corpus import conll2000, brown
grammar = r"""
    PP: {<RB|JJ\$>?<IN>}
        {<TO|VBG>} # e.g. to, regarding
"""

parser = nltk.RegexpParser(grammar)
for sentence in brown.tagged_sents()[:10]:
    tree = parser.parse(sentence)
    print(tree)

################# Questão 5 #################

print('>>> Questão 5 >>>')
chunked = [
    ("the", "DT"), ("receiving", "VBG"), ("end","NN"),
    ("assistant", "NN"), ("managing","VBG"), ("editor", "NN")
]
parser = nltk.RegexpParser("GER: {<DT>?<NN>?<VBG><NN>}")
print(parser.parse(chunked))

################# Questão 6 #################
print('>>> Questão 6 >>>')

chunked = [
    ("July","NNP"), ("and","CC"), ("August","NNP"), ("all", "DT"),
    ("your", "PRP$"), ("managers", "NNS"), ("and", "CC"),
    ("supervisors", "NNS"), ("company","NN"), ("courts","NNS"),
    ("and","CC"), ("adjudicators","NNS")
]
parser = nltk.RegexpParser(
    """CNP: {<NNP><CC><NNP>|<DT><PRP\$><NNS><CC><NNS>|<NN><NNS><CC><NNS>}"""
)
print(parser.parse(chunked))
