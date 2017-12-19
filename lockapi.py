#!/usr/local/bin/python3

from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from lockingserver import lockingserver 

app = Flask(__name__)
api = Api(app)



class locking_server_api():
    def __init__(self):
        global lockserver
        self.file_server = file_server
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('message', type=dict, location='json')
        super(locking_server_api, self).__init__()
    
    # going to return a if a spesific file is locked 
    def get(self, _id):
        kwargs = self.reqparse.parse_args()
        self.file_locked = self.lockserver.check_files_locked(**kwargs)
        if self.file_locked is not None:
            this_dir = self.dir_server.get_one_dir_form_name(name, **kwargs)
        else:
            this_dir = self.dir_server.get_one_dir_form_args(**kwargs)
        if this_dir is not None:
            return {'retrived dir' : this_dir}
        else:
            return {'error' : 'directory not found'}

    # going to try and lock a file 
    def post(self, _id):
        kwargs = self.reqparse.parse_args()
        self.lock = self.file_locked.lock_file(**kwargs)
        if self.lock is not None:
            if 'locked' in self.lock:
                return {'file locked': _id}
            elif 'file locked'
                return {'error' : 'file could not be locked as already locked!' + ' id: 'str(_id)}
        else:
            return {'error': 'No message'}

    # unlock a file 
    def put(self, _id):
        kwargs = self.reqparse.parse_args()
        self.unlock = self.file_locked.unlock_file(**kwargs)
        if self.unlock is not None:
            if 'file unlocked' in self.unlock:
                return {'file unlocked': _id}
            else:
                return {'error' : 'file could not be unlocked'}
        else:
            return {'error' : 'Message was empty'}




api.add_resource(locking_server_api, '/locked',endpoint= 'locked')

if __name__ == '__main__':
    lockserver = lockingserver()
    app.run(host = '0.0.0.0', debug=True, port=8050)






