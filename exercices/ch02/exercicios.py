#####################################
#            Exercício 4            #
#####################################
import nltk
from nltk.corpus import state_union

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in state_union.fileids()
    for w in state_union.words(fileid)
    for target in ['men', 'women', 'people']
    if w.lower() == target
)
# cfd.plot()


#####################################
#            Exercício 5            #
#####################################

from nltk.corpus import wordnet

def relations(noun):
    noun_synset = wordnet.synset(noun)
    print('Member Meronyms:\n ')
    print(noun_synset.member_meronyms())
    print('\nPart Meronyms:\n')
    print(noun_synset.part_meronyms())
    print('\nSubstance Meronyms:\n')
    print(noun_synset.substance_meronyms())
    print('\nMember Holonyms:\n')
    print(noun_synset.member_holonyms())
    print('\nPart Holonyms:\n')
    print(noun_synset.part_holonyms())
    print('\nSubstance Holonyms:\n')
    print(noun_synset.substance_holonyms())

relations('tree.n.02')

#####################################
#            Exercício 8            #
#####################################

nomes = nltk.corpus.names
cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in nomes.fileids()
    for name in nomes.words(fileid)
)
# cfd.plot()

#####################################
#            Exercício 13           #
#####################################

syns = list(wordnet.all_synsets('n'))
no = []

for s in syns:
    if len(s.hyponyms()) == 0:
        no.append(s)

print((len(no) / len(syns)) * 100)

#####################################
#            Exercício 14           #
#####################################


def supergloss(s):

    hypernyms = '\n'.join([h.name() + ': ' + h.definition() for h in s.hypernyms()])
    hyponyms = '\n'.join([h.name() + ': ' + h.definition() for h in s.hyponyms()])

    text = (
        'Def: ' + s.definition() + '\n\n' + 'Hypernyms:{}\n\nHyponyms:{}\n'
    ).format(hypernyms, hyponyms)

    return text

#####################################
#            Exercício 17           #
#####################################

def most_frequent_content_words(text):
    stopwords = nltk.corpus.stopwords.words('english')
    non_stopwords = []
    for w in text:
        if w.lower() not in stopwords and any(c.isalpha() for c in w):
            non_stopwords.append(w.lower())

    fd = nltk.FreqDist(non_stopwords)
    return [w for w, num in fd.most_common(50)]

#####################################
#            Exercício 18           #
#####################################

def freqt_bigrams(text):
    stopwords = nltk.corpus.stopwords.words('english')
    bg = [b for b in nltk.bigrams(text) if b[0] not in stopwords and b[1] not in stopwords and any(c.isalpha() for c in b[0]) and any(c.isalpha() for c in b[1])]
    fd = nltk.FreqDist(bg)
    return [b for b, num in fd.most_common(50)]

#####################################
#            Exercício 25           #
#####################################

from nltk.corpus import udhr

def find_language(word):
    langs = []
    for f in udhr.fileids():
        if f.endswith('-Latin1') and word in udhr.words(f):
            langs.append(f[:-7])
    return langs

print(find_language('para'))

#####################################
#            Exercício 28           #
#####################################
from operator import itemgetter

tuples = [
    ('car', 'automobile'),
    ('gem', 'jewel'),
    ('journey', 'voyage'),
    ('boy', 'lad'),
    ('coast', 'shore'),
    ('asylum', 'madhouse'),
    ('magician', 'wizard'),
    ('midday', 'noon'),
    ('furnace', 'stove'),
    ('food', 'fruit'),
    ('bird', 'cock'),
    ('bird', 'crane'),
    ('tool', 'implement'),
    ('brother', 'monk'),
    ('lad', 'brother'),
    ('crane', 'implement'),
    ('journey', 'car'),
    ('monk', 'oracle'),
    ('cemetery', 'woodland'),
    ('food', 'rooster'),
    ('coast', 'hill'),
    ('forest', 'graveyard'),
    ('shore', 'woodland'),
    ('monk', 'slave'),
    ('coast', 'forest'),
    ('lad', 'wizard'),
    ('chord', 'smile'),
    ('glass', 'magician'),
    ('rooster', 'voyage'),
    ('noon', 'string')
]

lch = []
for word1, word2 in tuples:
    similarity = wordnet.lch_similarity(
        wordnet.synsets(word1)[0],
        wordnet.synsets(word2)[0]
    )
    triple = (word1, word2, similarity)
    lch.append(triple)
print(sorted(lch,key=itemgetter(2),reverse=True))
