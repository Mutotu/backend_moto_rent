from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.motorcyle import Motorcycle, MotoList, MotoModify
from resources.comment import Comment


from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'muto'
api = Api(app)



@app.route('/')
def home():
    return 'Hello ulen'



@app.before_first_request
def create_tables():
    db.create_all()



jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
api.add_resource(Motorcycle, '/post')
api.add_resource(MotoModify, '/moto/<int:id>')
api.add_resource(MotoList, '/motos')
api.add_resource(Comment, '/comment')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True) 