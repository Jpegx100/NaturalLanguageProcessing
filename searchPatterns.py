import nltk
from nltk.collocations import *
from nltk.corpus import mac_morpho
from nltk.tag import DefaultTagger
from nltk.tag import UnigramTagger
from nltk.chunk import RegexpParser
from nltk.tree import *

def ExtractPhrases(myTree, phrase):
	myPhrases = []
	if (myTree.label() == phrase):
		treeTmp = myTree.copy(True)
		word=""
		for w in treeTmp.leaves():
			if (len(word)==0):
				word = w[0]
			else:
				word = word+" "+w[0]
		myPhrases.append(word)
	for child in myTree:
		if (type(child) is Tree):
			list_of_phrases = ExtractPhrases(child, phrase)
			if (len(list_of_phrases) > 0):
				myPhrases.extend(list_of_phrases)
	return myPhrases

#Extração de padrões
etiqPadrao = DefaultTagger('N')  # Usando etiquetas default para os tokens nao reconhecidos
sentencas_treinadoras = mac_morpho.tagged_sents()[0:15000]
etiq = UnigramTagger(sentencas_treinadoras, backoff=etiqPadrao)
stopwords = nltk.corpus.stopwords.words("portuguese")

i=0
Negs=0
Pos=0
Neut=0
todosTokens=[]
todosTermos=[]
#while i < r.num_rows():
#while i < 1:
	#x=r.fetch_row()
	#coment=str(x[0][0],"utf8")
coment=str("cadeira velha")
tokens=nltk.word_tokenize(coment.lower())
tags = etiq.tag(tokens)
	#print(coment)
	#print(tags)
	#i=i+1

analiseGramatical = RegexpParser(r"""
		PADRAO7: {<N><ADJ>}
        PADRAO1: {<ADJ><N>(<PREP>?<N>)*}
        PADRAO2: {<ADV><ADV>?<ADJ>(<N>(<PREP>?<N>)*)?}
        PADRAO3: {<N>(<PREP>?<N>)*(<ADJ>)<ADV><ADV>?}
        PADRAO4: {<N>(<PREP>?<N>)*<ADV>?<ADJ>+}
        PADRAO5: {<ADV><V>}
        PADRAO6: {<V><ADV>}
		""")
arvore = analiseGramatical.parse(tags)
x1 = ExtractPhrases(arvore, "PADRAO1")
x2 = ExtractPhrases(arvore, "PADRAO2")
x3 = ExtractPhrases(arvore, "PADRAO3")
x4 = ExtractPhrases(arvore, "PADRAO4")
x5 = ExtractPhrases(arvore, "PADRAO5")
x6 = ExtractPhrases(arvore, "PADRAO6")
x7 = ExtractPhrases(arvore, "PADRAO7")
  	
