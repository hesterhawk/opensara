from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length

from app.config.dashboard import Customers

from app.models.customer import Customer

class UpdateCustomerForm(FlaskForm):

    instagram_login = StringField('instagram login', validators=[DataRequired(), Length(max=128)])    
    state = SelectField('State',
        default=0,
        choices = Customers.state,
        validators=[DataRequired()]
    )
    description = TextAreaField('description', validators=[Length(max=8000)])
    submit = SubmitField('Create new Customer')

    def set_customer_id(self,id):
        self.customer_id = id

    def validate_instagram_login(self, instagram_login):        
        customer = Customer.query.filter_by(instagram_login=instagram_login.data).first()

        if customer is None: return True

        if customer.id != self.customer_id:
            raise ValidationError('Sorry my Friend, instagram login is in use')