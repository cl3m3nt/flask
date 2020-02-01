from flask import Flask
app = Flask(__name__)

@app.route('/')
def index_page():
    return 'Welcome to index page!'

@app.route('/function1')
def function1():
    return 'Hello from function1!'

@app.route('/funcstringvar/<inputstring>')
def stringFunc(inputstring):
    return 'Welcome %s' %inputstring

@app.route('/funcintvar/<int:inputint>')
def intFunc(inputint):
    return 'You entered %d' %inputint
