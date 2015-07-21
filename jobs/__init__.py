from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config.from_object('config')


db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from jobs.controllers import app_jobs as jobs_application

app.register_blueprint(jobs_application)

db.create_all()


