"""Flask app for adopt app."""
from models import Pet
from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

from models import db, connect_db

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get("/")
def pets_list():
    """Show page which has list of all pets."""

    pets = Pet.query.all()

    return render_template("pets_list.html", pets=pets)


@app.route("/add/", methods=["GET", "POST"])
def add_pet():
    """form for adding a pet to the database"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        flash(f"Added {name} to the list!")

        # data = {name: name,
        # species: species,
        # photo_url: photo_url,
        # age: age,
        # notes: notes,
        # available: available}
        new_pet = Pet({name: name,
        species: species,
        photo_url: photo_url,
        age: age,
        notes: notes,
        available: available})

        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')

    else:
        return render_template(
            "add.html", form=form)


@app.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_pet(id):
    """Form for editing a pet in the database."""

    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Pet {id} updated!")
        return redirect(f"/{id}/edit")

    else:
        return render_template(
            "pet_details.html", form=form)
