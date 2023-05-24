from flask import Blueprint, request, jsonify
from services.substitute import get_synonyms, substitute
from services.pos_synonym import get_synonym_for_word_in_sentence

main_routes_bp = Blueprint('main_routes', __name__)

@main_routes_bp.route('/')
def index():
    return 'Welcome to the main page!'

@main_routes_bp.route("/synonyms/<string:word>")
def synonyms(word):
    return "<p>synonyms for " + word + "</p>" + get_synonyms(word).__str__()

@main_routes_bp.route("/substitute")
def check():
    sentence = request.args.get('sentence', type=str)
    words = request.args.get('word', type=str)
    return jsonify(substitute(sentence, words.split(',')))

# Example sentence: I condemn this, index: 1
@main_routes_bp.get("/pos_synonym")
def pos_synonym():
    sentence = request.args.get('sentence', type=str)
    ind = request.args.get('index', type=int)
    return get_synonym_for_word_in_sentence(sentence, ind)