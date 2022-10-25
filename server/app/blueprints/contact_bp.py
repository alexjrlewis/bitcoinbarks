from flask import Blueprint, jsonify, render_template, request
from flask_mail import Message
from app import mail
from app.forms.contact_form import ContactForm

contact_bp = Blueprint("contact_bp", __name__)


@contact_bp.route("/", methods=["GET"])
def get():
    form = ContactForm()
    return render_template("contact.html", form=form)


@contact_bp.route("/send-message", methods=["POST"])
def send_message():
    print(__name__, "send_message")
    form = ContactForm()
    print(form)
    print(form.email)
    print(form.subject)
    print(form.message)
    if form.validate_on_submit():
        msg = Message(
            "Hello from the other side!",
            sender="peter@mailtrap.io",
            recipients=["paul@mailtrap.io"],
        )
        msg.body = ""
        mail.send(msg)
        return "Message sent!"
    return
