from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CheckoutForm(FlaskForm):
    customer_name = StringField('Full Name', validators=[DataRequired()])
    customer_address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Place Order')
