from app import db
from flask import jsonify
from app.common.models import Base

    
class Category(Base):
    __tablename__ = "category"
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    imageUrl = db.Column(db.String(300), nullable=False) 

    def __init__(self, name, description, imageUrl):
        self.name = name
        self.description = description
        self.imageUrl = imageUrl
        
    def __repr__(self):
        return '<Title %r>' % (self.name)                        
