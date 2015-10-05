import nltk
from nltk.collocations import *
from nltk.corpus import mac_morpho
from nltk.tag import DefaultTagger
from nltk.tag import UnigramTagger
from nltk.chunk import RegexpParser
from nltk.tree import *


def ExtractPhrases(myTree, phrase):
        """Método que compara recursivamente em cada sub-árvore da
árvore(myTree) dada o padrão(phrase) requerido e retorna a
lista de frases nas quais este se faz presente."""
        myPhrases = []
	#Compara a label da árvore com o padrão a ser buscado
        if (myTree.label() == phrase):
                #Copia temporariamente a árvore
                treeTmp = myTree.copy(True)
                word=""
		#Pega cada tupla(palavra, tag) da árvore e concatena as palavras
                for w in treeTmp.leaves():
                        if (len(word)==0):
                                word = w[0]
                        else:
                                word = word+" "+w[0]
                #Adiciona a frase que corresponde ao padrão/arvore
                myPhrases.append(word)
	#Faz o processo ser repetido recursivamente para que o padrão(phrase)
	#seja procurado em cada um dos filhos da árvore e concatena o resultado
	#se este for favorável
        for child in myTree:
                if (type(child) is Tree):
                        list_of_phrases = ExtractPhrases(child, phrase)
                        if (len(list_of_phrases) > 0):
                                myPhrases.extend(list_of_phrases)
	#Retorna a lista de padrões encontrados
        return myPhrases

#Cria o etiquetador padrão para que palavras não conhecidas sejam tratadas com substantivo(N)
etiqPadrao = DefaultTagger('N')
#Pega o trainning set a partir das tagged_sents() do mac_morpho
sentencas_treinadoras = mac_morpho.tagged_sents()[0:15000]
#Cria o UnigramTagger com base no etiquetador padrão e treina-o com as sentenças etiquetadas do mac_morpho
etiq = UnigramTagger(sentencas_treinadoras, backoff=etiqPadrao)

coment = str(input("Entre com o texto: "))
if coment == "default":
        coment = open("default.txt", "r").read().replace("\n", " ")
#O texto é convertido em tokens
tokens=nltk.word_tokenize(coment.lower())
#É etiquetada cada token do texto
tags = etiq.tag(tokens)

#É criado o analisador de expresões regulares contendo os padrões procurados
analiseGramatical = RegexpParser(r"""
		PADRAO7: {<N><ADJ>}
        PADRAO1: {<ADJ><N>(<PREP>?<N>)*}
        PADRAO2: {<ADV><ADV>?<ADJ>(<N>(<PREP>?<N>)*)?}
        PADRAO3: {<N>(<PREP>?<N>)*(<ADJ>)<ADV><ADV>?}
        PADRAO4: {<N>(<PREP>?<N>)*<ADV>?<ADJ>+}
        PADRAO5: {<ADV><V>}
        PADRAO6: {<V><ADV>}
		""")
#O analisador é então utilizado para a geração da árvore de padrões
arvore = analiseGramatical.parse(tags)
x = [ExtractPhrases(arvore, "PADRAO1"), ExtractPhrases(arvore, "PADRAO2"),
     ExtractPhrases(arvore, "PADRAO3"), ExtractPhrases(arvore, "PADRAO4"),
     ExtractPhrases(arvore, "PADRAO5"), ExtractPhrases(arvore, "PADRAO6"),
     ExtractPhrases(arvore, "PADRAO7")]
for aux in range(len(x)):
        print("PADRAO 0"+str(aux+1)+str(x[aux]))
