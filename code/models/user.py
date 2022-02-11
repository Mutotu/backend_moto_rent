import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(80), nullable=True, unique=True)
    password = db.Column(db.String(80), nullable=True)
    first_name = db.Column(db.String(120), nullable=True)
    last_name = db.Column(db.String(120), nullable=False)
    age = db.Column( db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    # role = db.Column( db.String, nullable=False)
    
    # motorcycles = db.relationship("MotorcycleModel", backref="users", lazy='dynamic')
    # comments  = db.relationship("Comments", backref="users", lazy=True)
    # rents =  db.relationship("Rents", backref="users", lazy=True)
    

    
    def __init__(self, first_name, last_name, age, email,username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username
        self.password = password
        # self.role = role
        
    def json(self):
        return {
            "user":{
             "fn":   self.first_name,
             "ln": self.last_name,
             "age":self.age,
             'email':self.email,
             
            },"bikes": [bike.json() for bike in self.motorcycles.all()]
        }
        
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()