from tinydb import TinyDB, Query,where
m = 'CL-0'
def get_max(x):
    global m
    m = max(m,x)
    return False
    

db = TinyDB('./databases/Clients.json')
#db.purge()
print(db.all())
#res = db.search(where('uid').test(get_max))
#print(res,m)
'''db.insert({
            'uid': "CL-1",
            'First Name': "Jayaraman",
            'Last Name': "N R",
            'Date Of Birth' : "24-12-1999",
            'Phone' : "9600097849"
        })
db.insert({
            'uid': "CL-2",
            'First Name': "Jayaraman",
            'Last Name': "N R",
            'Date Of Birth' : "24-12-1999",
            'Phone' : "9600097849"
        })'''
db.close()