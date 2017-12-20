#!/usr/local/bin/python3 

import requests
from collections import defaultdict

# new_file = {
#     'id': self.filename_counter,
#     'name': message['name'],
#     'content': message['content'],
#     'your mom': messgae['your mom']
# }


class clientlib():
    def __inti__(self, name, port):
        self.server_add = 'http://127.0.0.1:8080/dirs/' 
        self.locking_add = 'http://127.0.0.1:8050/locking/'
        self.file_add = 'http://127.0.0.1:' + str(port) + '/file/'
        self.file_server = 'http://127.0.0.1:' + str(port + 10) + '/files/'
        self.cachename = []
        self.cached_files = defaultdict(list)
        self.cache_max = 10
        self.client_port = port
        self.name = name 
    
    # Descirater
    def print_response(f):
        def wrapped_f(*args, **kwargs):
            r = f(*args, **kwargs)
            print(r)
            print(r.json())
            return r
        return wrapped_f
    
    def kwargs(self, **kwargs):
        if 'message' in kwargs and kwargs['message'] is not None:
            return kwargs['message']
        else:
            return None

    @print_responce
    def cache_search(self, name):
        if name in self.cachename:
            return True
        else:
            return False

    # LRU! - cached on creatation, vewing, editing ( any action on file ) caches via name - if file smae name it wont add to cach
    @print_responce
    def cache_add(self, file_):
        name = file_['name']
        if name is not None:
            if self.cache_search(name) is True:
                return 'cached'
            else:
                if self.cache_max == 10:
                    self.cached_files.pop(self.cachename(-1))
                    self.cached_files[name] = file_ 
                    self.cachename.pop()
                    self.cachename.index(0, name)
                else:
                    self.cachename.index(0, name)
                    self.cached_files[name] = file_
                    self.cache_max += 1
                    return 'cached'
        else:
            return 'file has no name'

    # Returns the files that are cache
    @print_responce 
    def get_cached(self, name):
        if self.cache_search(name) is True:
            return self.cached_files[name] 
        else:
            return None 
             
    @print_responce
    def get_file_with_info(self, *args, **kwargs):
        if kwargs(**kwargs) is not None:
            message = kwargs(**kwargs)
        else:
            return None
        name = message['name']
        if 'name' in message and message['name'] is not None:
            if self.get_cached(name) is not None:
                return self.get_cached(name)
            else:
                return 'not in cache'
        if '_id' in message and message['_id'] is not None:
            return requests.get(self.server_add, json={'message': message})
        if self.cache_search(name) is False:
            # go get the file 
            return requests.get(self.server_add, json={'message': message})

    @print_responce
    def add_file(self, *args, **kwargs):
        if kwargs(**kwargs) is not None:
            message = kwargs(**kwargs)
            self.cache_add(message)
            return requests.post(self.server_add, json={'message': message})
        else:
            return None
                
    @print_responce
    def edit_file(self, *args, **kwargs):
        if kwargs(**kwargs) is not None:
            message = kwargs(**kwargs)
            locked = requests.get(self.locking_add, json={'message': message})
            if 'locked' in locked :
                return 'cant edit file, file is locked'
            else:
                lock_file = requests.post(self.locking_add, json={'message': message})
                if 'file locked' in lock_file:
                    editedfile = requests.put(self.file_add, json={'message': message})
                    requests.put(self.locking_add, json={'message': message})
                    return {'file edited': editedfile }
                else:
                    return 'file would not lock'

        


if __name__ == '__main__':
    print('going to do some real cool shit, wait till you see... just wait till you see!')
