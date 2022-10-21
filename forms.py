
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional



class AddPetForm(FlaskForm):
    """Form for adding a new pet"""

    name = StringField("Name", validators=[InputRequired()])

    species = SelectField('Species',
        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
        validators=[InputRequired()])

    photo_url = StringField("Photo Url", validators=[InputRequired()])

    age = SelectField('Age',
        choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')],
        validators=[InputRequired()])

    notes = TextAreaField('Notes', validators=[Optional()])

    available = BooleanField('Available for Adoption?', default="checked")


