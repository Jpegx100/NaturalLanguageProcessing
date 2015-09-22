import nltk
from nltk.corpus import brown

# Get the sents tagged from corpus
tagged_sents = brown.tagged_sents(categories='romance')
# Get the sents untagged from corpus
sents = brown.sents(categories='romance')
# Choose the slice size of training and test for the Tagger
# (90% in this case)
size = int(len(tagged_sents)*0.9)
# Create the Tagger with a slice sents tagged
bigram_tagger = nltk.BigramTagger(tagged_sents[:size])
# Print the evaluation of Tagger's performance with tested sents
print("Evaluation of tested sents   = "+
      str(bigram_tagger.evaluate(tagged_sents[:size])*100)[:5]+"%")
# Print the evaluation of Tagger's performance with untested sents
print("Evaluation of untested sents = "+
      str(bigram_tagger.evaluate(tagged_sents[size:])*100)[:5]+"%")
