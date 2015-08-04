from app import db
from flask import jsonify
from app.common.models import Base

    
class Category(Base):
    __tablename__ = "category"
    name = db.Column(db.String(128),  nullable=False)
    description = db.Column(db.Text,nullable=True)
    images = db.relationship('Category_Image', backref='category', lazy='dynamic')

    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __repr__(self):
        return '<Title %r>' % (self.name)                        
        
        
class Category_Image(Base):
    __tablename__ = "category_image"
    image_path = db.Column(db.String(300),  nullable=False)      
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    
    def __init__(self,image_path,category):
        self.image_path=image_path
        self.category = category
        
        