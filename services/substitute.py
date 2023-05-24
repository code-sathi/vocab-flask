import nltk

from nltk.corpus import wordnet

from services.hypernyms import hypernym_substitute
from services.hyponyms import replace_with_hyponym

def get_synonyms(word):
    synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def substitute(sentence,words):
    substitutes = []
    tokens = nltk.word_tokenize(sentence)
    for i in range(len(tokens)):
            synonyms = set()
            for syn in wordnet.synsets(tokens[i]):
                for lemma in syn.lemma_names():
                    synonyms.add(lemma)

            for each in synonyms:
                if each in words:
                    tokens[i] = each
                    break
    substitutes.append({"synonym_replacement":" ".join(tokens)[:-2]+"."})
    substitutes.append({"hypernym_replacement":hypernym_substitute(sentence)[:-2]+"."})
    substitutes.append({"hyponym_replacement":replace_with_hyponym(sentence)})
    return substitutes