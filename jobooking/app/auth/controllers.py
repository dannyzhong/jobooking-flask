from app import app,db
from app.auth.models import User,Role
from flask.ext.security import Security, SQLAlchemyUserDatastore

            


# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

import json
# Import the database object from the main app module
from app import db
# Import module forms

# Import module models (i.e. User)
from app.category.models import Category

from flask_security import auth_token_required


def init_security():
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

# Define the blueprint: 'auth', set its url prefix: app.url/auth
app_auth = Blueprint('auth', __name__, url_prefix='/auth')

#@app_auth.route('/', methods=['GET'])