from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import os

from dotenv import load_dotenv

# no longer needed
# from security import authenticate, identity
from resources.user import UserRegister, UserLogin, User
from resources.motorcyle import Motorcycle, MotoList, MotoModify
from resources.comment import Comment
from resources.rent import Rent,RentedMotos


from db import db


app = Flask(__name__)
load_dotenv(".env")
# app.config("DEBUG") = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'muto'
api = Api(app)
db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app,db)




@app.before_first_request
def create_tables():
    db.create_all()




api.add_resource(UserRegister, '/register')
api.add_resource(Motorcycle, '/post')
api.add_resource(MotoModify, '/moto/<int:id>')
api.add_resource(MotoList, '/motos')
api.add_resource(Comment, '/comment/<int:moto_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(RentedMotos, '/rent/<int:rent_id>')
api.add_resource(Rent, '/rent/<int:moto_id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True) 