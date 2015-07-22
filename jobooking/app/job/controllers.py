# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for


# Import the database object from the main app module
from app import db

# Import module forms

# Import module models (i.e. User)
from app.job.models import job

# Define the blueprint: 'auth', set its url prefix: app.url/auth
app_jobs = Blueprint('jobs', __name__, url_prefix='/jobs')

# Set the route and accepted methods
@app_jobs.route('/', methods=['GET', 'POST'])

def test():
    return "testing"

                

