from db import db


class MotorcycleModel(db.Model):
    
    __tablename__ ='motorcycles' 
       
    id = db.Column( db.Integer, primary_key=True)
    
    make = db.Column( db.String, nullable=False)
    model=db.Column( db.String, nullable=False)
    year=db.Column(db.String, nullable=False)
    price=db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    photo = db.Column(db.String, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('UserModel', backref="users", uselist=False)
    # rents = db.relationship("RentModel", backref="motorcycles", lazy=True,cascade="all,delete")
    comments = db.relationship("CommentModel", backref="motorcycles",  uselist=False,cascade="all,delete")
    
    def __init__(self,user_id, make,model,year,price,description,photo):
        self.user_id = user_id
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.description = description
        self.photo = photo
        
    def json(self):
        return {
            "motorcycle" : {
            "id":self.id,
            # "user_id": user_id,
            'make':self.make,
            'model':self.model,
            'year':self.year,
            'price':self.price,
            'description':self.description,
            'photo':self.photo
            }, 
            # "comments":[comment.json() for comment in self.comments.all()]
        }
        
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    
    
            
    def save_to_db(self):
        
        db.session.add(self)      
        db.session.commit()


    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()