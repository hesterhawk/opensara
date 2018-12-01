from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

from app.models.customer import Customer

class CreateCustomerForm(FlaskForm):

    instagram_login = StringField('instagram login', validators=[DataRequired(), Length(max=128)])    
    state = IntegerField('State', validators=[DataRequired()])
    submit = SubmitField('Create new Customer')

    def validate_instagram_login(self, instagram_login):        
        customer = Customer.query.filter_by(instagram_login=instagram_login.data).first()

        if customer is not None:                
            raise ValidationError('Sorry my Friend, instagram login is in use')