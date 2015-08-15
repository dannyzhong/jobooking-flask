from app import db
from flask import jsonify
from app.common.models import Base

    
class Category(Base):
    __tablename__ = "category"
    name = db.Column(db.String(128),  nullable=False)
    description = db.Column(db.Text,nullable=True)
    search_count = db.Column(db.BigInteger, default = 0)
    image = db.relationship('Category_Image', uselist=False, backref='category')
    

    def __init__(self, name,description,image,search_count=None):
        self.name = name
        self.search_count = search_count
        self.description = description
        self.image = image
        
        
    def __repr__(self):
        return '<Title %r>' % (self.name)                        
        
        
class Category_Image(Base):
    __tablename__ = "category_image"
    image_path = db.Column(db.String(300),  nullable=False)      
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    
    def __init__(self,image_path):
        self.image_path=image_path
        
        
        