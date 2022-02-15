from flask_restful import Resource, reqparse
from models.rent import RentModel
from models.motorcycle import MotorcycleModel
#to get the headers
from flask import request



class Rent(Resource):
    
    parser = reqparse.RequestParser()
    
    parser.add_argument('start_date', 
                        type=str, 
                        required=True, 
                        help="This field cannot be left blank")
    
    parser.add_argument('end_date',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )





    def post(self, moto_id):
        
        data = Rent.parser.parse_args()
        user_id = request.headers.get('user_id')
        # moto_id = request.headers.get('moto_id')
    
        moto = MotorcycleModel.find_by_id(id=moto_id)

        if moto:

                rented = RentModel(user_id, moto_id, data["start_date"], data["end_date"], )

                try:
                   
                    rented.save_to_db()
                except Exception as e:
                    print(e)
                    return {'message': 'An error occured while creating a rent'}
        
                return rented.json()
    
        return {'message':'Moto doesn\'t exist'}
        
        
class RentedMotos(Resource):
        #to test to see if the rent table saves the data
    def get(self, rent_id):
        data = Rent.parser.parse_args()
        rental = RentModel.find_by_id(id=rent_id)
        
        return rental.json()
        
        
