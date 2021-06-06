from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AnimalNameSubmit(FlaskForm):

    name = StringField('name', validators = [DataRequired()])
    submit = SubmitField('Generate')