import nltk
#Criar a sentença como uma lista de tuplas(palavra, classe)
sentence = [("O","DT"), ("garoto","NN"), ("jogou", "VBD"), ("bola", "NN"),
            ("com", "DT"), ("os","DT"), ("amigos", "NNS")]
#Criar a regra gramátical dos padrões procurados
grammar = """PADRAO: {<DT>+(<NN>|<NNS>)+}"""

#Transformar a regra gramátical em um analisador de expressões regulares (Arvore)
cp = nltk.RegexpParser(grammar)

#Usar o analisador para encontrar o padrão da sentença
result = cp.parse(sentence)
print(result)
