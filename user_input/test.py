# importing the libraries
from flask import Flask, request

# creating flask application object
# __name__ -> variable that evaluates name to the current python module
app = Flask(__name__)

# we want to call this function from somewhere else
# def addition(a, b):
#     return a + b

# accessing the function with help of decorator
# to run -> copy the labs location
# https://blue-librarian-ftzrc.pwskills.app/
# then add port number
# https://blue-librarian-ftzrc.pwskills.app:5000/
# then add @app.route('/adddition') i.e. to add /addition
# https://blue-librarian-ftzrc.pwskills.app:5000/addition
@app.route('/addition')
def addition():
    return f"This is my test function"

# https://blue-librarian-ftzrc.pwskills.app:5000/sudh
@app.route('/sudh')
def print_name():
    return f"Sudhanshu Kumar"

# using request package
# https://blue-librarian-ftzrc.pwskills.app:5000/user
# input will be provided with help of an url adding ?variable_name='input'
# for e.g. https://blue-librarian-ftzrc.pwskills.app:5000/user?name=sudhanshu 
# (where name is variable and sudhanshu is user input you can change that as you want)
@app.route('/user')
def print_user():
    data = request.args.get('name')
    return f"{data}"

if __name__ == '__main__':
    app.run(host = '0.0.0.0')