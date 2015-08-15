from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Configurations
app.config.from_object('config')
app.config['SECRET_KEY'] = 'super-secret'

db = SQLAlchemy(app)

# Setup Flask-Security


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from job.controllers import app_jobs as jobs_mod
from nest.controllers import app_nest as nest_mod
from timetable.controllers import app_timetables as timetables_mod
from category.controllers import app_category as category_mod
from auth import controllers as auth_ctl
app.register_blueprint(jobs_mod)
app.register_blueprint(nest_mod)
app.register_blueprint(timetables_mod)
app.register_blueprint(category_mod)
auth_ctl.init_security()

db.create_all()

