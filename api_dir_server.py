#!/usr/local/bin/python3

from flask import Flask
from flask_restful import Api, Resource
from flask_restful import reqparse
from dir_file_server import dir_file_server 

app = Flask(__name__)
api = Api(app)
# This is the main hub of commiunication
# This is used to comm between usr and the DFS
# add file, add serevr
######## These two will be done in client lib ###########
# delete, edit, find file 
# lock file (when editing)


class dir_server_api(Resource):
    def __init__(self):
        global dir_server
        self.dir_server = dir_server
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('message', type=dict, location='json')
        super(dir_server_api, self).__init__()

    def get(self):
        kwargs = self.reqparse.parse_args()
        return {'message' : self.dir_server.get_file(**kwargs)}


class dir_add(Resource):
    # the args it is expecting 
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('_id', type=str, location='json')
        self.reqparse.add_argument('fileserver', type=str, location='json')
        super(dir_server_api, self).__init__()
    
    # this will add the filesever
    def get(self):
        kwargs = self.reqparse.parse_args()
        fileserver = self.dir_server.add_file_server(**kwargs)
        if fileserver is not None:
            return {'file server added': fileserver}
        else:
            return {'error': 'file server coudl not be added'}

    # this will add an indvidual file to server 
    def post(self):
        kwargs = self.reqparse.parse_args()
        f = self.dir_server.add_one_file(**kwargs)
        if f is not None:
            return {'file added': f}
        else:
            return {'error': 'file could not be added'}

        
api.add_resource(dir_server_api, '/dir/', endpoint='dir')
api.add_resource(dir_add, '/dir/add', endpoint='add')


if __name__ == '__main__':
    dir_server = dir_file_server()
    app.run(host='0.0.0.0', debug=True, port=8080)
