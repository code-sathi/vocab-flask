from flask import Flask, request
import nltk
from nltk.corpus import wordnet
from services.hyponyms import replace_with_hyponym
from services.hypernyms import hypernym_substitute

app = Flask(__name__)
nltk.download('wordnet')
nltk.download('omw-1.4')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/synonyms/<string:word>")
def synonyms(word):
    return "<p>synonyms for " + word + "</p>" + get_synonyms(word).__str__()

@app.route("/substitute")
def check():
    sentence = request.args.get('sentence', type=str)
    words = request.args.get('word', type=str)
    return substitute(sentence, words.split(','))

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