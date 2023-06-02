import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# Set the secret key
app.config['SECRET_KEY'] = 'mysecretkey'

# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb+srv://starxaway:sparta@cluster0.ddlu9am.mongodb.net/'

# Initialize PyMongo
mongo = PyMongo(app)

# Blueprint registration and URL prefixes
from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(puppies_blueprint, url_prefix='/puppies')
