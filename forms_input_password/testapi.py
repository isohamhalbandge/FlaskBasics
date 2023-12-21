# importing the libraries
from flask import Flask, request, jsonify, render_template

# create application object
app = Flask(__name__)

# Importing html file
@app.route('/') # '/' -> home folder or directory
def show_form():
    return render_template('index.html')

# checking user details
@app.route("/process_form", methods=['POST'])
def check_userdetails():
    name = request.form.get('username')
    password = request.form.get('password')
    print({name}, {password})
    return "username and password recieved"

if __name__ == "__main__":
    app.run(host='0.0.0.0')