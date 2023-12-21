# Importing the libraries
# TODO : We can add logging and exception handling as we want

from flask import Flask, render_template, request
app = Flask(__name__)

# getting the inputs from html form
@app.route("/")
def calculator_page():
  return render_template('index.html')

# setting up route 
@app.route("/math", methods = ['POST'])
def calculator_test():  
  ops = request.form['operation'] # tells which kind of operation is being performed
  first_num = int(request.form['num1']) # takes the num1 input 
  second_num = int(request.form['num2']) # takes the num2 input
  
  # assigning the tasks for operations

  # for addition
  if(ops == 'add'):
    result = first_num + second_num
    return f"Addition of {first_num} and {second_num} is {result} "

  # for subtraction
  if(ops == 'subtract'):
    result = first_num - second_num
    return f"Subtraction of {first_num} and {second_num} is {result} "

  # for multiplication
  if(ops == 'multiply'):
    result = first_num * second_num
    return f"Multiplication of {first_num} and {second_num} is {result} "

  # for division
  if(ops == 'divide'):
    result = first_num / second_num
    return f"Divison of {first_num} and {second_num} is {result} "

# main function

if __name__ == '__main__':
  app.run(host = '0.0.0.0')
