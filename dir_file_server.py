#!/usr/local/bin/python3

import requests
from collections import defaultdict
import json
from local_file_server import local_file_server 


class dir_file_server():
    def __init__(self):
        self.machine_id_counter = 1
        self.machines = defaultdict(dict)
        # machines = {
        #         id1 = { 
                        # 'files' :[file_server_id1, file_server_id2],
                        # 'name' : name
                        # 'id' : _id
                        # },
        #         }


    def get_files_on_all_servers(self, *args, **kwargs):
        # parse args
        if 'message' in kwargs and kwargs['message'] is not None:
            message = kwargs['message']
        else:
            return None

        all_files_servers = []
        all_files = []
        if 'show_files' in message:

        # get files on all machines
        for mahcine in machines:
            for server in machine:
                
                all_files_servers.append(server)
        
            
        # call get files on all files

        # return list of file info -> name 
        pass
    

def add_dir(self, *args, **kwargs):
    # parse args
    if 'message' in kwargs and kwargs['message'] is not None:
        message = kwargs['message']
    else:
        return None

    if 'name' in message: 
        new_dir = {}
        
   


    pass

def get_one_dir_form_name(self,name, *args, **kwards):
    # parse args

    # search for machine id and return 

    pass

def get_one_dir_form_args(self, *args, **kwargs):
    pass


def get_next_id(self):
    next_id = self.machine_id_counter
    self.machine_id_counter += 1
    return next_id 

def update_dir(self, _id, *args, **kwargs):
    # tbc 
    pass



