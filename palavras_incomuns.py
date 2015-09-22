import nltk
def palavras_incomuns(text):
	text_v = set(w.lower() for w in text if w.isalpha())
	english_v = set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_v - english_v
	return sorted(unusual)
 
print(palavras_incomuns('Jon is dead and baaaad'))