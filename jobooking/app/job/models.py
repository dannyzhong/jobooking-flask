from app import db
from app.jobookee.models import Jobookee
from flask import jsonify
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

    
class Job(Base):
    __tablename__ = "job"
    job_title = db.Column(db.String(128),  nullable=False)
    job_desc = db.Column(db.Text,nullable=True)
    jobookee_id = db.Column(db.Integer, db.ForeignKey('jobookee.id'))
    images = db.relationship('Image', backref='job', lazy='dynamic')

    def __init__(self, job_title,job_desc,jobookee):

        self.job_title     = job_title
        self.job_desc = job_desc
        self.jobookee = jobookee
        

    def __repr__(self):
        return '<Title %r>' % (self.job_title)                        
        
        
class Image(Base):
    __tablename__ = "job_image"
    image_path =    db.Column(db.String(300),  nullable=False)      
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    
        
    def __init__(self,image_path,job):
        self.image_path=image_path
        self.job = job
        
        