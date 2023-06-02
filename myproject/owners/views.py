from flask import Blueprint, render_template, redirect, url_for
from myproject.models import Puppy
from myproject.owners.forms import AddOwner

owners_blueprint = Blueprint('owners', __name__, template_folder='templates')

@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddOwner()
    if form.validate_on_submit():
        owner = form.name.data
        id = form.id.data
        pup = Puppy.query.get(id=id)  # Assuming Puppy is an SQLAlchemy model
        pup.owner = owner
        pup.save()
        return redirect(url_for('puppies.list'))
    return render_template("owners/add_owner.html", form=form)
