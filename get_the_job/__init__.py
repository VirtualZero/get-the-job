

from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']
csrf = CSRFProtect(app)


from get_the_job.main.routes import main_routes