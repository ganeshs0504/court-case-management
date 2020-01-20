from flask import Flask,render_template,request,session,abort,flash,redirect,Response
import os
import uuid
from tinydb import TinyDB, Query,where
from datetime import date
app = Flask(__name__)
client_db = TinyDB('./databases/Clients.json')
m = 'CL-0'
def get_max(x):
    global m
    m = max(m,x)
    return False
    
def get_id():
    client_db.search(where('uid').test(get_max))
    return 'CL-'+str(int(m.split('-')[1])+1)


@app.route('/',methods=['GET'])
def handle_home():
    if not session.get('logged_in',False):
        return render_template('login.html')
    return render_template('main.html',user_data=session['user_data'])

@app.route('/login',methods=['POST'])
def handle_login():
    ''' Check User with database '''
    data = request.form
    if data['password'] == '123' and data['username'] == 'admin@123':
        session['logged_in'] = True
        session['user_data'] = {'username':data['username']}
    else:
        flash('Incorrect Username or Password')
    return redirect('/')

@app.route('/register',methods=['GET','POST'])
def handle_register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        ''' Check User with database '''
        return redirect('/')

@app.route('/logout',methods=['GET'])
def handle_logout():
    session['logged_in'] = False
    return redirect('/')

@app.route('/clients',methods=['GET','POST'])
def handle_client():
    if not session.get('logged_in',False):
        return render_template('login.html')
    if request.method == 'POST':
        form = request.form
        id = get_id()
        path = './static/files/clients/'+id
        os.mkdir(path)

        client = {
            'uid': id,
            'First Name': form['fname'],
            'Last Name': form['lname'],
            'Date Of Birth' : form['dob'],
            'Phone' : form['phone'],
            'Start Date' : form['start_date'],
            'Files' : []
        }
        for files in request.files.values():
            files.save(path+'/'+files.filename)
            client['Files'].append(path+'/'+files.filename)
        client_db.insert(client)
        # clients = client_db.all()
 
        return redirect('/clients')
    else:
        clients = client_db.all()
        for x in clients:
            year,month,day = map(int,x['Date Of Birth'].split('-'))
            x['age'] = (int((date.today() - date(year,month,day)).days / 365.2425 ) )
        return render_template('add_client.html',user_data = session['user_data'],clients=clients)


@app.route('/clients/<id>',methods=['GET'])
def handle_get_client(id):
    if not session.get('logged_in',False):
        return render_template('login.html')
    u = Query()
    res = client_db.search(u.uid == id)
    print(res)
    # try:
    return render_template('client.html',client_data=res[0],user_data=session['user_data'])
    # except:
    #     return 'No'

    

# @app.errorhandler(404) 
# def invalid_route(e): 
#     return render_template('404.html')



if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(port=3000)