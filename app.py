"""Flask app for adopt app."""
from models import Pet
from flask import Flask, render_template, flash
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
        return redirect('/add')

    else:
        return render_template(
            "add.html", form=form)
