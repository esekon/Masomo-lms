from flask import Flask,request, make_response, jsonify
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import stripe


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///student_portal.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = True
app.config["SECRET_KEY"] = "92256b9d8a05214dab4362d83c9e17d1"
stripe.api_key = 'sk_test_51PBjHERtUzKvr3OfRNcqNVOSi6tCnZioSXRYsMsHhTOYBhWqc6q1bF5KvSZEWLMDHLUUP5tyVFMnx3qWCz9c6yfu00CsZmFKWM'

app.config["STRIPE_API_KEY"] = stripe.api_key

app.json.compact=False
db =SQLAlchemy()
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
db.init_app(app)
CORS(app)