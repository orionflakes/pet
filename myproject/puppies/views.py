# File: myproject/puppies/views.py

from flask import Blueprint, render_template, redirect, url_for, flash
from myproject.models import Puppy
from myproject.puppies.forms import AddForm, DeleteForm
from flask_mongoengine import MongoEngine

puppies_blueprint = Blueprint('puppies', __name__, template_folder='templates')
db = MongoEngine()

# Initialize the MongoDB connection
def initialize_db(app):
    app.config['MONGODB_SETTINGS'] = {
        'db': 'your_database_name',
        'host': 'your_mongodb_host',
        'port': 27017,  # default MongoDB port
        # additional MongoDB settings if needed
    }
    db.init_app(app)

@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        owner = form.owner.data
        new_pup = Puppy(name=name, owner=owner)
        new_pup.save()
        flash(f"We added {new_pup.name} to our database!")
        return redirect(url_for('puppies.list'))
    return render_template("puppies/add.html", form=form)

@puppies_blueprint.route('/list')
def list():
    puppies = Puppy.objects.all()
    return render_template("puppies/list.html", puppies=puppies)
