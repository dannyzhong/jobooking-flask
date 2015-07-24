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
    jobookee = db.relationship('Jobookee',
        backref=db.backref('jobs', lazy='dynamic'))

    def __init__(self, job_title,job_desc,jobookee):

        self.job_title     = job_title
        self.job_desc = job_desc
        self.jobookee = jobookee
        

    def __repr__(self):
        return '<Title %r>' % (self.job_title)                        
    def to_json(self):
        list = []
        test = dict(ttt="1")
        list.append(test)
        list.append(test)
        
        json_str = dict(title=self.job_title, test=list);
        
        return jsonify(json_str)
        
        
        
        
        
        