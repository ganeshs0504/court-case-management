import uuid
class User:
    def __init__(self,a,b):
        self.username = a
        self.password = b
    def get_json(self):
        return {'username':self.username,'password':self.password,'uid':str(uuid.uuid4())}

from tinydb import TinyDB, Query,where
db = TinyDB('test.json')
u = Query()
print(db.search(where('username').test(lambda x: len(x) == 7)))