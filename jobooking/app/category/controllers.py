
# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

import json
# Import the database object from the main app module
from app import db
# Import module forms

from sqlalchemy import desc,asc
# Import module models (i.e. User)
from app.category.models import Category

from flask_security import auth_token_required, http_auth_required
from django.template.defaultfilters import default

# Define the blueprint: 'auth', set its url prefix: app.url/auth
app_category = Blueprint('category', __name__, url_prefix='/category')

@app_category.route('/', methods=['GET'])
#@auth_token_required
#@http_auth_required
def show_categories():
    sortby = request.args.get('sortby')
    limit = request.args.get('limit')
    
    category_objects = Category.query.order_by(asc(sortby)).limit(int(limit))
    
    category_list = []
    for item in category_objects:
        category_list.append(dict(id = item.id,name = item.name,description = item.description))
        
    
    
    
    return jsonify(dict(result = category_list)) 

# Set the route and accepted methods

@app_category.route('/<category_id>', methods=['GET'])
def show_category_detail(category_id):
    category_object = Category.query.get()
    image_list = []
    
    for image in category_object.images.all():        
        image_list.append(dict(image_path = image.image_path))
    
    category_detail = dict(id = category_object.id,
                      name = category_object.name,
                      description = category_object.description,
                      image = image_list)
    
    return jsonify(category_detail) 
                

