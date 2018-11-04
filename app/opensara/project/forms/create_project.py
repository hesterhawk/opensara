from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

from app.models.project import Project

class CreateProjectForm(FlaskForm):

    fullname = StringField('Fullname', validators=[DataRequired(), Length(min=6, max=10)])

    submit = SubmitField('Sign In')