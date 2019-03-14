from get_the_job import app
from flask import render_template


@app.route('/')
def landing():
    return render_template(
        'main/landing.html',
        title="Portfolio"
    )