from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/function1')
def function1():
    return 'Hello from function1!'

@app.route('/function2')
def function2():
    return 'Hello from function2!'
