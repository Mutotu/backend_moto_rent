from flask_restful import Resource, reqparse
from models.comment import CommentModel
#to get the headers
from flask import request


class Comment(Resource):
    
    parser = reqparse.RequestParser()
    
    # parser.add_argument('user_id', 
    #                     type=int, 
    #                     required=True, 
    #                     help="This field cannot be left blank")
    
    # parser.add_argument('moto_id',
    #                     type=int,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('comment',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    # parser.add_argument('date',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
  
  
  
    def post(self):
        data = Comment.parser.parse_args()
        user_id = request.headers.get('user_id')
        moto_id = request.headers.get('moto_id')
        data['user_id'] = user_id
        data["moto_id"] = moto_id
        print(data, "###ERE#@$#$##!###$")
        
        comment = CommentModel(**data)
        
        try:
            comment.save_to_db()
        except:
            return {'message': 'An error occred while creating a comment'}, 500
        return comment.json(), 201