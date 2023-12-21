# importing the libraries
from flask import Flask, request, jsonify, render_template

# create application object
app = Flask(__name__)

# Importing html file
@app.route('/')
def show_form():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')