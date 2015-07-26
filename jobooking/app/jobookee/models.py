from app import db
from sqlalchemy.orm import backref

class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

    
class Jobookee(Base):
    __tablename__ = "jobookee"
    jobookee_name = db.Column(db.String(128),  nullable=False)
    jobs = db.relationship('Job', backref='jobookee',lazy='dynamic')
    

    def __init__(self, jobookee_name):

        self.jobookee_name     = jobookee_name
        

    def __repr__(self):
        return '<Jobookee Name %r>' % (self.jobookee_name)          