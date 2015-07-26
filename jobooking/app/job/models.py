from app import db
from app.jobookee.models import Jobookee
from flask import jsonify
from app.common.models import Base

    
class Job(Base):
    __tablename__ = "job"
    job_title = db.Column(db.String(128),  nullable=False)
    job_desc = db.Column(db.Text,nullable=True)
    nest_id = db.Column(db.Integer, db.ForeignKey('nest.id'))
    images = db.relationship('Job_Image', backref='job', lazy='dynamic')



    def __init__(self, job_title,job_desc,jobookee):

        self.job_title     = job_title
        self.job_desc = job_desc
        self.jobookee = jobookee
        

    def __repr__(self):
        return '<Title %r>' % (self.job_title)                        
        
        
class Job_Image(Base):
    __tablename__ = "job_image"
    image_path =    db.Column(db.String(300),  nullable=False)      
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    
        
    def __init__(self,image_path,job):
        self.image_path=image_path
        self.job = job
        
        