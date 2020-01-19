class User:
    def __init__(self,email,fname,lname,password):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.password = password
    def to_json(self):
        return {
            'email':self.email,
            'first_name':self.fname,
            'last_name': self.lname,
            'password' : self.password
        }
    