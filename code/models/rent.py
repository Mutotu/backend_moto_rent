from db import db

class RentModel(db.Model):
    
    __tablename__ = 'rents'
    
    id=db.Column( db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    moto_id = db.Column(db.Integer, db.ForeignKey('motorcycles.id'))
    start_date = db.Column( db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    confirmed = db.Column(db.Boolean)
   
    def __init__(self, user_id, moto_id, start_date, end_date):
        self.user_id = user_id
        self.moto_id = moto_id
        self.start_date = start_date
        self.end_date = end_date
        # self.total_price=total_price
        self.confirmed = False
        
    def json(self):
        return {
            "rent_info":{
                'id':self.id,
            'moto_id':self.moto_id,
            'start_date':self.start_date,
            'end_date':self.end_date,
            'total_price':self.total_price,
            'confirmed':self.confirmed
            }
           
        }
    def charge_total(self,moto_id):
        days = int(self.end_date[-2:]) - int(self.start_date[-2:])
        
        
        moto_qs = Motorcycles.query.filter_by(id=moto_id)
        print(moto_qs)
        
        if moto_qs:
            moto = moto_qs.first()
            print(moto)
            print(moto.price)
            return moto.price * days
        return 0  