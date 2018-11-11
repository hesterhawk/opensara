from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

from app.models.project import Project

class CreateProjectForm(FlaskForm):

    fullname = StringField('Fullname', validators=[DataRequired(), Length(max=128)])

    submit = SubmitField('Sign In')