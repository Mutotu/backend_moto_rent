from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

# no longer needed
# from security import authenticate, identity
from resources.user import UserRegister, UserLogin, User
# from resources.motorcyle import Motorcycle, MotoList, MotoModify
# from resources.comment import Comment


from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'muto'
api = Api(app)



@app.route('/')
def home():
    return 'Hello ulen'



@app.before_first_request
def create_tables():
    db.create_all()



jwt = JWTManager(app)

api.add_resource(UserRegister, '/register')
# api.add_resource(Motorcycle, '/post')
# api.add_resource(MotoModify, '/moto/<int:id>')
# api.add_resource(MotoList, '/motos')
# api.add_resource(Comment, '/comment')
api.add_resource(UserLogin, '/login')
api.add_resource(User, '/user/<int:user_id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True) 