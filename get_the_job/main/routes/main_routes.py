from get_the_job import app
from get_the_job.forms.forms import ContactForm
from flask import render_template, jsonify, abort, send_file
import os
import requests


@app.route('/')
def landing():
    contact_form = ContactForm()
    return render_template(
        'main/landing.html',
        title="Portfolio",
        contact_form=contact_form
    )


@app.route('/submit-message', methods=['POST'])
def submit_message():
    contact_form = ContactForm()

    if contact_form.validate_on_submit():
        send_message = requests.post(
            'https://mailapi.virtualzero.tech/mail/send-mail',
            headers={
                'X-API-KEY': os.environ['MAIL_API_KEY']
            },
            json={
                "recipients": ["birtchum@virtualzero.net"],
                "subject": "New message from Portfolio",
                "message": make_message(contact_form)
            }
        )

        return jsonify(
            {
                'status': 'success'
            }
        ), 200

    else:
        errors = {}

        for fieldName, errorMessages in contact_form.errors.items():
            errors[fieldName] = errorMessages[0]

        return jsonify(
            {
                'status': 'error',
                'errors': errors
            }
        ), 400


def make_message(contact_form):
    return f"Here are the details of the message:\n" \
           f"First Name: {contact_form.contact_first_name.data}\n" \
           f"Last Name: {contact_form.contact_last_name.data}\n" \
           f"Email: {contact_form.contact_email.data}\n" \
           f"Phone: {contact_form.contact_phone.data}\n" \
           f"Message: {contact_form.message.data}"


@app.route('/download/Birtchum_Thompson_Resume.docx')
def download_getip_vm():
    try:
        return send_file(
            'static/resume/Birtchum_Thompson_Resume.docx',
            attachment_filename='Birtchum_Thompson_Resume.docx'
        )

    except:
        abort(500)
