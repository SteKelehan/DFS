#!/usr/local/bin/python3 

import request

class clientlib():
    def __inti__(self):
        self.server_add = ''
        self.file_add = ''
        self.file_server = ''
        self.locking_add = ''
        self.cache_id = []
        self.cached_files = {}
        self.cache_max = 10
    
    # Descirater
    def print_response(f):
        def wrapped_f(*args, **kwargs):
            r = f(*args, **kwargs)
            print(r)
            print(r.json())
            return r
        return wrapped_f

    @print_responce
    def cache_search(self, _id):
        pass

    @print_responce
    def cache_add(self, _id):
        pass

    

    @print_responce
    def get_file_and_with_info(self, _id):
        pass

    @print_responce
    def add_file(self, _id):
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
