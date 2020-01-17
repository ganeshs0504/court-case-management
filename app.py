from flask import Flask,render_template

app = Flask(__name__)

@app.route('/hello')
def handle():
    return render_template('test.html',l=['123','45'])

if __name__ == '__main__':
    app.run()