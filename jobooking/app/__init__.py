from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config.from_object('config')


db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from job.controllers import app_jobs as jobs_mod

from jobookee.controllers import app_jobookees as jobookees_mod
app.register_blueprint(jobs_mod)

app.register_blueprint(jobookees_mod)
db.create_all()