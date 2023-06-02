from flask import Flask, render_template
from myproject.models import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['MONGODB_SETTINGS'] = {
    'db': 'petadopt',
    'host': 'localhost',
    'port': 27017,
}

db.init_app(app)

@app.route('/')
def index():
    return render_template('home.html')

# Import blueprints
from myproject.owners.views import owners_blueprint
from myproject.puppies.views import puppies_blueprint

# Register blueprints
app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(puppies_blueprint, url_prefix='/puppies')

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=5000)
