"""Flask app for adopt app."""

from flask import Flask

from flask_debugtoolbar import DebugToolbarExtension

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

    


# @app.get('/users')
# def users_index():
#     """Show a page with info on all users"""

#     users = User.query.order_by(User.last_name, User.first_name).all()
#     return render_template('users/index.html', users=users)