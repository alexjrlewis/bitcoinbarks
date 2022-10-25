from flask_wtf import FlaskForm, RecaptchaField
from wtforms import BooleanField, SelectField, SubmitField, StringField, TextAreaField
import wtforms.validators as validators


class PayForm(FlaskForm):

    # recaptcha = RecaptchaField()

    submit = SubmitField(
        "Send",
        render_kw={
            "class": "button-primary-hollow",
            "style": "color: white; text-transform: none; font-size: initial;",
        },
    )
