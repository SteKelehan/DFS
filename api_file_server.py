#!/usr/local/bin/python3

from flask import Flask
from flask_restful import Api, Resource
from flask_restful import reqparse
from local_file_server import local_file_server

app = Flask(__name__)
api = Api(app)

# This class Api deals with individual files 

class file_server_api(Resource):
    def __init__(self):
        # allowing access to insitence of local file server
        global file_server
        self.file_server = file_server
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('message', type=dict, location='json')
        super(file_server_api, self).__init__()

    def get(self, _id):
        kwargs = self.reqparse.parse_args()
        if _id != 0:
            this_file = self.file_server.get_one_file_from_id(_id, **kwargs)
        else:
            this_file = self.file_server.get_one_file_from_args(**kwargs)
        if this_file is not None:
            return {'retrieved file': this_file}
        else:
            return {'error': 'file not found'}

    def post(self, _id):
        kwargs = self.reqparse.parse_args()
        this_file = self.file_server.add_file(**kwargs)
        if this_file is not None:
            return {'created file': this_file}
        else:
            return {'error': 'file not created'}

    def put(self, _id):
        kwargs = self.reqparse.parse_args()
        this_file = self.file_server.edit_file(_id, **kwargs)
        if this_file is not None:
            return {'edited file': this_file}
        else:
            return {'error': 'file not edited'}

    def delete(self, _id):
        kwargs = self.reqparse.parse_args()
        this_file = self.file_server.delete_file(_id, **kwargs)
        if this_file is not None:
            return {'deleted file': this_file}
        else:
            return {'error': 'file not deleted'}


# going to adda boolean for locking server
# 'done': fields.Boolean,
file_fields = {
    'name': fields.String,
    'uri': fields.Url('task')
}

class file_api(Resouurce):
    def __init__(self):
        # alowing acess to local file serve
        global file_server
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('message', type = dict, location='json')
        super(file_api, self).__init__()
    
   # Get all files from server 
   def get(self):
       kwargs = self.reqparse.parse_args()
       if self.files is None:
           return {'error':'No files on file server'}
       else:
           return {'files' : [marshal(file_, file_fields) for file_ in self.files]}
    
    # This deletes the file sever - not sure if will be NotImplemented
    def delete(self):
        kwargs = self.reqparse.parse_args()
        if self.files is None:
            return {'error' : 'Server is alreay empty'}
        else:
            return


            



api.add_resource(file_api, '/file/<int:_id>', endpoint='file')
api.add_resource(file_server_api, '/files/', endpoint='files')

if __name__ == '__main__':
    file_server = local_file_server()
    port = sys.args[1]
    app.run(host='0.0.0.0', debug=True, port=int(port))
