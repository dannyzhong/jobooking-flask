from app import db
from app.jobookee.models import Jobookee

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

    def __init__(self, job_title,job_desc,jobookee_id):

        self.job_title     = job_title
        

    def __repr__(self):
        return '<Title %r>' % (self.job_title)                        
