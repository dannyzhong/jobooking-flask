from app import db

from flask import jsonify
from app.common.models import Base

    
class Job(Base):
    __tablename__ = "job"
    job_title = db.Column(db.String(128),  nullable=False)
    job_desc = db.Column(db.Text,nullable=True)
    
    nest_id = db.Column(db.Integer, db.ForeignKey('nest.id'))
    nest = db.relationship('Nest', backref='job')
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship("Category", backref="job")
    
    job_image_id = db.Column(db.Integer, db.ForeignKey('job_image.id'))
    image = db.relationship('Job_Image', backref='job')



    def __init__(self, job_title,job_desc,category,image,nest):
        self.job_title     = job_title
        self.job_desc = job_desc
        self.category = category
        self.image = image
        self.nest = nest
    

    def __repr__(self):
        return '<Title %r>' % (self.job_title)                        
        
        
class Job_Image(Base):
    __tablename__ = "job_image"
    image_path =    db.Column(db.String(300),  nullable=False)      
    
    
        
    def __init__(self,image_path):
        self.image_path=image_path
        
        
        