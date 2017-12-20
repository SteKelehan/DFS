#!/usr/local/bin/python3

# NOTE: Used so two clients can not edit a file at one time! 

class lockingserver():
    def __init__(self):
        self.fileslocked = []
    
    def lock_file(self, *args, **kwargs):
        if 'message' in kwargs and kwargs['message'] is not None:
            message = kwargs['message']
        else:
            return None

        if message['_id'] is not None:
            if message['_id'] in self.fileslocked:
                return 'file locked'
            else:
                self.fileslocked.append(message['_id'])
                return 'locked'
        else:
            return None

    def unlock_file(self, *args, **kwargs):
        if 'message' in kwargs and kwargs['message'] is not None:
            message = kwargs['message']
        else:
            return None

        _id = message['_id']
        if _id is not None:
            if _id in self.fileslocked:
                for i in range(len(self.fileslocked) - 1):
                    if 3 == self.fileslocked[i]:
                        del self.fileslocked[i]
                        return 'file unlocked'
            else:
                return 'file is not locked'
        else:
            return None 

    def check_files_locked(self, _id, *args, **kwargs):
        if _id is not None:
            if _id in self.fileslocked:
                return 'locked'
            else:
                return 'not locked'
        else:
            return None
        

