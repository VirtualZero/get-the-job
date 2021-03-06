

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_assets import Environment, Bundle
from flask_htmlmin import HTMLMIN
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']
app.config['DEBUG'] = False
app.config['MINIFY_PAGE'] = True
htmlmin = HTMLMIN(app)
csrf = CSRFProtect(app)


# Assets
#app.config['FLASK_ASSETS_USE_CDN'] = True
assets = Environment(app)

js = Bundle(
    'js/materialize.min.js',
    'fontawesome/fontawesome-all.min.js',
    'js/smooth-scroll.polyfills.min.js',
    'js/app.js',
    output='assets/get-the-job.js',
    filters='jsmin'
)

css = Bundle(
    'css/style.css',
    output='assets/get-the-job.css',
    filters='cssmin'
)

assets.register('get_the_job_js', js)
assets.register('get_the_job_css', css)


from get_the_job.main.routes import main_routes
from get_the_job.errors.routes import error_routes
