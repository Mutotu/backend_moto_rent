from flask_restful import Resource, reqparse
from models.motorcycle import MotorcycleModel
#to get the headers
from flask import request

class Motorcycle(Resource):
    
    
    
    parser = reqparse.RequestParser()
    
    parser.add_argument('make', 
                        type=str, 
                        required=True, 
                        help="This field cannot be left blank")
    
    parser.add_argument('model',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('year',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('price',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('photo',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    # parser.add_argument('user_id',
    #                     type=int,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    # ##########3 not receving user_id 
    def post(self):
        data = Motorcycle.parser.parse_args()
        user_id = request.headers.get('user_id')
        data['user_id'] = user_id
        motorcycle = MotorcycleModel(**data)
        print(data,"#########")
        print(motorcycle,"#########")
      
        try:
            motorcycle.save_to_db()
        except: 
              return {'message': 'An error occured while creating the post'}, 500
        return motorcycle.json(), 201
        
    
    def get(self, id):
        motorcycle = MotorcycleModel.find_by_id(id)
        if motorcycle:
            return motorcycle.json()
        return {'message': "Motorcycle not found"}

        
    def delete(self, id):
        motorcycle = MotorcycleModel.find_by_id(id)
        if motorcycle:
            motorcycle.delete_from_db()
        return {"message": "Item deleted"}
 
 
    def put(self, id):
        data = Motorcycle.parse_arg()
        motorcycle = MotorcycleModel.find_by_id(id)
        if id is None:
            motorcycle = MotorcycleModel(id, data['make'], data['model'], data['year'], data['price'], data['description'], data['photo'])
        else:
            motorcycle = {**data}
        motorcycle.save_to_db()
        
        return data.json()
    
    
    
    
    class MotoList(Resource):
        def get(self):
            return {'motos': [moto.json() for moto in MotorcycleModel.query.all()]}