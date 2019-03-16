from wtforms.validators import DataRequired, Length, email
from wtforms import StringField, IntegerField, TextAreaField, ValidationError
from flask import request
from flask_wtf import FlaskForm


class ContactForm(FlaskForm):
    def validate_math(form, field):
        if field.data > 18 or \
           field.data < 0 or \
           (int(request.form['rand_num1']) +
                int(request.form['rand_num2'])) != field.data:

            raise ValidationError(
                'The answer to the math problem is incorrect.'
            )

    contact_first_name = StringField(
        "First Name *",
        [
            DataRequired(),
            Length(
                max=100,
                message="First name cannot exceed 100 characters."
            )
        ]
    )

    contact_last_name = StringField(
        "Last Name *",
        [
            DataRequired(),
            Length(
                max=100,
                message="Last name cannot exceed 100 characters."
            )
        ]
    )

    contact_email = StringField(
        "Email *",
        [
            DataRequired(),
            email(),
            Length(
                max=150,
                message="Email address cannot exceed 150 characters."
            )
        ]
    )

    contact_phone = StringField(
        "Phone",
        [
            Length(
                max=14,
                message="Phone number cannot exceed 16 characters."
            )
        ]
    )

    message = TextAreaField(
        "What's on your mind?",
        [
            DataRequired(),
            Length(
                max=500,
                message="Message cannot exceed 500 characters."
            )
        ]
    )

    math_result = IntegerField(
        "Please solve the math problem.",
        [
            DataRequired(
                message="This field is required and must be an integer."
            ),
            validate_math
        ]
    )
