from flask import Flask
import nltk
from nltk.corpus import wordnet

app = Flask(__name__)
nltk.download('wordnet')
nltk.download('omw-1.4')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/synonyms/<string:word>")
def synonyms(word):
    return "<p>synonyms for " + word + "</p>" + get_synonyms(word).__str__()


def get_synonyms(word):
    synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())
    return synonyms