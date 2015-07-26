from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for


# Import the database object from the main app module
from app import db
from flask import request
# Import module forms

# Import module models (i.e. User)
from app.timetable.models import Timetable

# Define the blueprint: 'auth', set its url prefix: app.url/auth
app_timetables = Blueprint('timetables', __name__, url_prefix='/timetables')

# Set the route and accepted methods
@app_timetables.route('/', methods=['GET'])

def show_timetables():
    return request.args.get('job_id')

