from flask_restful import Resource, reqparse
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
    parser.add_argument('total_price',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

