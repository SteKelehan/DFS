#!/usr/local/bin/python3 

import request
from collections import defaultdict

# new_file = {
#     'id': self.filename_counter,
#     'name': message['name'],
#     'content': message['content'],
#     'your mom': messgae['your mom']
# }

class clientlib():
    def __inti__(self, port):
        self.server_add = 'http://127.0.0.1:' + str(port) + '/dirs/' 
        self.file_add = 'http://127.0.0.1:' + str(port + 20) + '/file/'
        self.file_server = 'http://127.0.0.1:' + str(port + 10) + '/files/'
        self.locking_add = 'http://127.0.0.1:' + str(port + 30) + '/locking/'
        self.cachename = []
        self.cached_files = defaultdict(list)
        self.cache_max = 10
        self.client_port = port 
    
    # Descirater
    def print_response(f):
        def wrapped_f(*args, **kwargs):
            r = f(*args, **kwargs)
            print(r)
            print(r.json())
            return r
        return wrapped_f

    @print_responce
    def cache_search(self, name):
        if name in self.cachename:
            return True
        else:
            return False

    # LRU! - cached on creatation, vewing, editing ( any action on file ) caches via name - if file smae name it wont add to cach
    @print_responce
    def cache_add(self, name):
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

    def get_cached(self, name):
        if self.cache_search(name) is True:
            return self.cached_files[name] 
        else:
            return None 
             

    @print_responce
    def get_file_with_info(self, *args, **kwargs):
        if 'message' in kwargs and kwargs['message'] is not None:
            message = kwargs['message']
        else:
            return None
        if 'name' in message and message['name'] is not None:
            if self.get_cached(name) is not None:
                return self.get_cached(name)
            else:
                return 'not in cache'

        if '_id' in message and message['_id'] is not None:
            return requests.get(self.)

        if cache_search(name) is False:
            # go get the file 
            return requests.get()

    @print_responce
    def add_file(self, *args, **kwargs):
        pass

    @print_responce
    def edit_file(self, *args, **kwargs):
        pass

    @print_responce
    def delete_file(self, *args, **kwargs):
        pass

    @print_responce
    def See_all_files(self, *args, **kwargs):
        pass








if __name__ == '__main__':
    print('going to do some real cool shit, wait till you see... just wait till you see!')
