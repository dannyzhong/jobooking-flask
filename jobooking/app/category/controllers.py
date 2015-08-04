
# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

import json
# Import the database object from the main app module
from app import db
# Import module forms

# Import module models (i.e. User)
from app.category.models import Category

# Define the blueprint: 'auth', set its url prefix: app.url/auth
app_category = Blueprint('category', __name__, url_prefix='/category')

@app_category.route('/', methods=['GET'])
def show_categories():
    return "show all categories"

# Set the route and accepted methods
@app_category.route('/<category_id>', methods=['GET'])
def show_category_detail(category_id):
    category_object = Category.query.get(category_id);
    
    image_list = []
    for image in category_object.images.all():        
        image_list.append(dict(image_path = image.image_path))
    
    
    category_detail = dict(id = category_object.id,
                      name = category_object.name,
                      description = category_object.description,
                      image = image_list)
    
    return jsonify(category_detail) 
                

