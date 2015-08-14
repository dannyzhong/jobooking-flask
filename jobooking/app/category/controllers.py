
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

def dict_category(category):
    category_detail = dict(id = category.id,
                      name = category.name,
                      description = category.description,
                      imageUrl = category.imageUrl)
    
    return category_detail

@app_category.route('/', methods=['GET'])
def show_categories():
    categories = Category.query.all();

    lcategory = []
    for cat in categories:
        lcategory.append(dict_category(cat))
    
    return jsonify(dict(categories = lcategory))

# Set the route and accepted methods
@app_category.route('/<category_id>', methods=['GET'])
def show_category_detail(category_id):
    category_object = Category.query.get(category_id);
    
    return jsonify(dict_category(category_object))
                

