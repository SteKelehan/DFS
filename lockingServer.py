#!/usr/local/bin/python3


class lockingserver():
    def __init__(self):
        self.fileslocked = []
    
    def lock_file(self, _id, *args, *kwargs):
        if _id is not None:
            if _id in self.fileslocked:
                return {'error' : 'file locked '}
            else:
                self.fileslocked.append(_id)
                return {'locked' : _id}
        else:
            return {'error' : 'file id is not valid'}

    def unlock_file(self, _id, *args, **kwargs):
        if _id is not None:
            if _id in self.fileslocked:
                for i in range(len(self.fileslocked) - 1):
                    if 3 == self.fileslocked[i]:
                        del self.fileslocked[i]
                        return {'file unlocked' : _id}
            else:
                return {'error' : 'file is not locked'}
        else:
            return {'error' : 'file id was None'}

    def check_files_locked(self, _id, *args, **kwargs):
        if _id is not None:
            if _id in self.fileslocked:
                return {'locked' : _id}
            else:
                return {'not locked' : _id}
        else:
            return {'error' : 'file id is not vailid'}
        
# if __name__ == '__man__':
    # print('Dont thin I will need a main, but here you go')

