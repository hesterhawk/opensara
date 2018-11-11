from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

from app.models.project import Project

class CreateCustomerForm(FlaskForm):

    fullname = StringField('Fullname', validators=[DataRequired(), Length(max=128)])
    submit = SubmitField('Create new Customer')