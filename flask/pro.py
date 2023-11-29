from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_welcome():
    return render_template('home.html')

@app.route('/add')
def hello():
    return render_template('add.html')

@app.route('/index')
def hi():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True,port=8002)

    