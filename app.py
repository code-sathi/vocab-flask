from flask import Flask, request,jsonify
import nltk
from nltk.corpus import wordnet
from services.hyponyms import replace_with_hyponym
from services.hypernyms import hypernym_substitute
from routes.routes import main_routes_bp

app = Flask(__name__)
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('punkt')

app.register_blueprint(main_routes_bp)

if __name__ == '__main__':
    app.run()