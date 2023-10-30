# Put your app in here.
from flask import Flask, request
from operations import add ,sub, mult , div

app = Flask(__name__)
@app.route("/math/add")
def adding_math():
    a = int(request.args["a"])
    b= int(request.args["b"])
    sum = add(a,b)
    return f"<h1>{sum}</h1>"
@app.route("/math/sub")
def subract_math():
    a = int(request.args["a"])
    b= int(request.args["b"])
    difference = sub(a,b)
    return f"<h1>{difference}</h1>"
@app.route("/math/mult")
def multiply_math():
    a = int(request.args["a"])
    b= int(request.args["b"])
    product = mult(a,b)
    return f"<h1>{product}</h1>"
@app.route("/math/div")
def divide_math():
    a = int(request.args["a"])
    b= int(request.args["b"])
    quotient = div(a,b)
    return f"<h1>{quotient}</h1>"

@app.route("/add")
def adding():
    a = int(request.args["a"])
    b= int(request.args["b"])
    sum = add(a,b)
    return f"<h1>{sum}</h1>"
@app.route("/sub")
def subract():
    a = int(request.args["a"])
    b= int(request.args["b"])
    difference = sub(a,b)
    return f"<h1>{difference}</h1>"
@app.route("/mult")
def multiply():
    a = int(request.args["a"])
    b= int(request.args["b"])
    product = mult(a,b)
    return f"<h1>{product}</h1>"
@app.route("/div")
def divide():
    a = int(request.args["a"])
    b= int(request.args["b"])
    quotient = div(a,b)
    return f"<h1>{quotient}</h1>"
if __name__ == "__main__":
    app.run(FLASK_ENV="environement")