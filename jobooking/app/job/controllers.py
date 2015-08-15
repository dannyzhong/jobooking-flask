
# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify


import json
# Import the database object from the main app module
from app import db
# Import module forms

# Import module models (i.e. User)
from app.job.models import Job, Job_Image
from app.nest.models import Nest

# Define the blueprint: 'auth', set its url prefix: app.url/auth
app_jobs = Blueprint('jobs', __name__, url_prefix='/jobs')

@app_jobs.route('/', methods=['GET'])

def show_all_jobs():
    return "show all jobs"

# Set the route and accepted methods
@app_jobs.route('/<job_id>', methods=['GET'])
def show_job_detail(job_id):
    job_object = Job.query.get(job_id);
   
    
    image_list = []
    for image in job_object.images.all():        
        image_list.append(dict(image_path = image.image_path))
    
    
    
    
    job_detail = dict(job_title = job_object.job_title,
                      job_desc = job_object.job_desc,
                      
                      images = image_list)
    
    
    
    return jsonify(job_detail) 
                

