from flask import Flask
from routes.routes import main_routes_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('punkt')

app.register_blueprint(main_routes_bp)