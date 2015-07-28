from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for


# Import the database object from the main app module
from app import db

# Import module forms

# Import module models (i.e. User)
from app.nest.models import Nest

# Define the blueprint: 'auth', set its url prefix: app.url/auth
app_nest = Blueprint('nest', __name__, url_prefix='/nest')

# Set the route and accepted methods
@app_nest.route('/', methods=['GET'])

def test():
    return "testing"