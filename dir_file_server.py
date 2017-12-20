#!/usr/local/bin/python3

import requests
from collections import defaultdict

# TODO: make file's get id from dir server 


class dir_file_server():
    def __init__(self):
        self.dir_id_counter = 1
        self.dirs = defaultdict(list)
        self.file_server = 'http://localhost:' 
        # Has a list of file server Ids 
        # dir = { 
        #         id1 : [fileid1, fileid2, fileid3],
        #         id2 : [fileid4, fileid5],
        #         id3_: [fileid6, fileid7, fileid8]
        #         }

    def kwargs(self, **kwargs):
        if 'message' in kwargs and kwargs['message'] is not None:
            return kwargs['message']
        else:
            return None

    def get_files_on_all_servers(self, *args, **kwargs):
        message = self.kwargs(**kwargs)
        if message is None:
            return None
        else:
            add = []
            for k in self.dirs.iterkeys():
                x = requests.get(self.file_server + str(k) + '/files', **kwargs)
                add.append(x)
            return add
            
    # TODO!
    def add_file_server(self, *args, **kwargs):
        message = self.kwargs(**kwargs)
        if message is None:
            return None
        else:
            return requests.post()


    def add_one_file(self, args, **kwargs):
        message = self.kwargs(**kwargs)
        if message is None:
            return None
        else:
            min = 300
            for keys in self.file_server:
                x = len(self.file_server[keys])
                if x < min:
                    min = x
                    key = keys  
            return requests.post(self.file_server + str(key) + '/file', **kwargs)

    def get_file(self, *args, **kwargs):
        message = self.kwargs(**kwargs)
        if message is None:
            return None
        else:
            if '_id' in message and message['_id'] is not None:
                # get key that file is in! -> gives file port
                key = [k for k, v in self.dirs.iteritems() if message['_id'] in v]
                key = key[0]
                return requests.get(self.file_server + str(key) + '/file', json={'_id': message['_id']})
            else:
                if 'name' in message and message['name'] is not None:
                    all_files = self.get_files_on_all_servers(message['name'])
                    return all_files 
                else:
                    return None



                
                
                



