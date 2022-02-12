from db import db



class CommentModel(db.Model):
    
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    moto_id =db.Column(db.Integer, db.ForeignKey('motorcycles.id'))
    title = db.Column(db.String(20), nullable=False)
    comment = db.Column(db.String(120), nullable=False)

    
    def __init__(self, user_id, moto_id, title, comment):

        self.user_id = user_id
        self.moto_id= moto_id
        self.title = title
        self.comment = comment
        
     
    def json(self):
        return {
            "comment":{
            "id":self.id,
            "user_id":self.user_id,
            "moto_id":self.moto_id,
            "title": self.title,
            "comment": self.comment,
        }
        
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