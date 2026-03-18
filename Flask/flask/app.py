from flask import Flask

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

## WSGI Application
app = Flask(__name__)

@app.route('/') # / = homepage
def welcome():
    return 'Welcome to this best Flask course. This should be amazing'

@app.route('/index')
def index():
    return 'Welcome to index page'

if __name__ == '__main__':
    app.run(debug=True)