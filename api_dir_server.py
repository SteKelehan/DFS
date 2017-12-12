#!/usr/local/bin/python3

from flask import Flask
from flask_restful import Api, Resource
from flask_restful import reqparse
from dir_file_server import dir_file_server 

app = Flask(__name__)
api = Api(app)

class dir_server_api(Resource):
    def __init__(self):
        global dir_server
        self.dir_server = dir_server
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('message', type=dict, location='json')
        super(dir_server_api, self).__init__()

    def get(self, name):
        kwargs = self.reqparse.parse_args()
        if name != '':
            this_dir = self.dir_server.get_one_dir_form_name(name, **kwargs)
        else:
            this_dir = self.dir_server.get_one_dir_form_args(**kwargs)
        if this_dir is not None:
            return {'retrived dir' : this_dir}
        else:
            return {'error' : 'directory not found'}

    def post(self, name):
        kwargs = self.reqpares.parse_args()
        this_dir = self.dir_server.add_dir(**kwargs)
        if this_dir is not None:
            return {'create dir' : this_dir}
        else:
            return {'error' : 'dir was not created'}

        

    def put(self, _id):
        kwargs = self.reqparse.parse_args()
        this_dir = self.dir_server.add_dir(**kwargs)
        if this_dir is not None:
            return {'created dir' : this_dir}
        else:
            return {'error': 'dir could not be created'}

    def delete(self, _id):
        # tbd
        pass


api.add_resource(dir_server_api, '/dirs/<string:name>',endpoint= 'dirs')

if __name__ == '__main__':
    dir_server = dir_file_server()
    app.run(host = '0.0.0.0', debug=True, port=8050)
