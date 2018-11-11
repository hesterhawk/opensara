from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

from app.models.project import Project

class CreateCustomerForm(FlaskForm):

    instagram_login = StringField('instagram login', validators=[DataRequired(), Length(max=128)])    
    state = IntegerField('State', validators=[DataRequired()])
    submit = SubmitField('Create new Customer')