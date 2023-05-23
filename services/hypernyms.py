import nltk

from nltk.corpus import wordnet


def get_hypernym(word):
    synset = wordnet.synsets(word)[0]
    hypernyms = synset.hypernyms()
    if hypernyms:
        return hypernyms[0].lemmas()[0].name()
    else:
        return word


def hypernym_substitute(sentence):
    words = nltk.word_tokenize(sentence)
    result = []
    for word in words:
        if nltk.pos_tag([word])[0][1] == 'NN':
            hypernym = get_hypernym(word)
            result.append(hypernym)
        else:
            result.append(word)
    return " ".join(result)