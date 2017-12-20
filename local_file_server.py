#!/usr/local/bin/python3
from collections import defaultdict
import requests 

# keeps all files on this server given by the dir server - uses a dic pf dics
# when file serer called / inits -> give all files to dir server (id's)
# add server to dir server
# add file
# edit file
# delete file
# find file

# TODO: Commit and figure out how ID works 

class local_file_server():
    def __init__(self, _id):
        self.files = defaultdict(dict)
        # files = { id1: {
        #     '_id':3,
        #     'name':'test',
        #     'content':'hello world',
        #     'your mum':'no'
        #     }
        # }
        # will have to move counter to dir server
        self.file_id_counter = 1
        self.dir_server = 'http://localhost:8080/dirs'
        self._id = _id 

    # getting file/files from dic given prams     
    def get_one_files_from_args(self, *args, **kwargs):
        if 'message' in kwargs and kwargs['message'] is not None:
            message = kwargs['message']
        else:
            return None

        if '_id' in message:
            key = message['_id']
            # call get from id *
            this_file = self.get_one_file_from_id(key)
        elif 'name' in message:
            key = message['name']
            searchfiles = []
            for key in self.files:
                this_file = self.files[key]
                searchfiles.append(this_file)
            return searchfiles
        else:
            return None

    # get file with id  
    def get_one_file_from_id(self, _id, *args, **kwargs):
        if _id in self.files:
            this_file = self.files[_id]
        else:
            print('cant get file')
            print('files', self.files)
            print('id', _id)
            print('type', type(_id))
            return None

        # filter
        filtered = ['_id']
        this_file = {k: v for k, v in this_file.items() if k not in filtered}

        # return filerded file ***
        return this_file

    # adding a file to this local file server 
    def add_file(self, *args, **kwargs):
        # parse argsA ***
        if 'message' in kwargs and kwargs['message'] is not None:
            message = kwargs['message']
        else:
            return None

        must_haves = ['name', 'content']
        # check args ***
        if not all(must_have in message for must_have in must_haves):
            return None
        # create file *
        new_file = {k: message[k] for k in must_haves}
        # new_file = {
        #     '_id': self.file_id_counter,
        #     'name': message['name'],
        #     'content': message['content'],
        #     'your mom': messgae['your mom']
        # }
        _id = self.get_next_id()
        new_file['_id'] = _id
        new_file['url'] = "http://127.0.0.1:8050/file/" + str(_id)
        self.files[_id] = new_file
        return new_file

    # this adds a new file id 
    def get_next_id(self):
        next_id = self.file_id_counter
        self.file_id_counter += 1
        return next_id

    # edits a file 
    def edit_file(self, _id, *args, **kwargs):
        # parse args ***
        if 'message' in kwargs and kwargs['message'] is not None:
            message = kwargs['message']
        else:
            return None
        # check args ***
        filtered = ['_id']
        edits = {
            k: v
            for k, v in message.items() if k not in filtered and v is not None
        }

        # check for name
        # get file *
        this_file = self.get_one_file_from_id(_id)
        if this_file is None:
            return None
        # edit file *
        for k, v in edits.items():
            this_file[k] = v

        # save file *sd
        self.files[_id] = this_file
        return this_file

    # deletes a file 
    def delete_file(self, _id, *args, **kwargs):
        # get file *
        if _id in self.files:
            this_file = self.files[_id]
            del self.files[_id]
            return this_file
        else:
            return None

######################   Need to com with dir!     ############################

    # add file serever to dir server -> want to send the server id and port 
    def add_to_server(self):
        # ask to be added to the dir server! 
        requests.get(self.dir_server + '/add',json={'filesever_url': 'http://localhost:'+str(self.port), 'fileserver':self._id} ).json()


    def add_all_files(self):
        # give files on local file server to dir server -> only id's 
        for files in self.files:
            requests.post(self.dir_server + '/add', json={'file_id':files['_id'], 'fileserver':self._id}).json()

            

    def add_a_file(self, _id):
        requests.post(self.dir_server + '/add', jsoni={'file_id':_id, 'fileserver':self._id}).json()
        
                
