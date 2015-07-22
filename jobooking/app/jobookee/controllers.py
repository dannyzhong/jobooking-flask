from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for


# Import the database object from the main app module
from app import db

# Import module forms

# Import module models (i.e. User)
from app.jobookee.models import jobookee

# Define the blueprint: 'auth', set its url prefix: app.url/auth
app_jobookees = Blueprint('jobookees', __name__, url_prefix='/jobookees')

# Set the route and accepted methods
@app_jobookees.route('/', methods=['GET', 'POST'])

def test():
    return "testing2"