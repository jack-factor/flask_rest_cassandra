# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from config import DevelopmentConfig
from views import ViewUser

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('lastname', type=str, required=True)
parser.add_argument('email', type=str, required=True)
parser.add_argument('phone', type=int, required=True)


class AllUser(Resource):
    def get(self):
        return jsonify({'users': ViewUser.getList()})

    def post(self):
        parser_args = parser.parse_args()
        # save record
        return jsonify({'users': ViewUser.save(parser_args)})


class UserOne(Resource):

    def get(self, pk):
        return jsonify({'user': ViewUser.getByID(pk)})

    def put(self, pk):
        parser_args = parser.parse_args()
        parser_args['id'] = pk
        return jsonify({'result': ViewUser.update(parser_args)})

    def delete(self, pk):
        return jsonify({'result': ViewUser.deleteByID(pk)})


api.add_resource(AllUser, '/users')
api.add_resource(UserOne, '/user/<uuid:pk>')

if __name__ == "__main__":
    # db.init_app(app)
    app.run(debug=True, port=8080)
