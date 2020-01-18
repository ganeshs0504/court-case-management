from flask import Flask,render_template,request,session,abort,flash,redirect
import os
app = Flask(__name__)

@app.route('/',methods=['GET'])
def handle_home():
    if not session.get('logged_in',False):
        return render_template('login.html')
    return render_template('main.html')

@app.route('/login',methods=['POST'])
def handle_login():
    ''' Check User with database '''
    data = request.form
    if data['password'] == '123' and data['username'] == 'admin@123':
        session['logged_in'] = True
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
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(port=3000)