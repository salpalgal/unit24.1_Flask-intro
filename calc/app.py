# Put your app in here.
from flask import Flask, request
from operations import add ,sub, mult , div

app = Flask(__name__)



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





@app.route("/math/<mathing>")

def all_math(mathing):
    
    a = int(request.args["a"])
    b= int(request.args["b"])
    math ={"add":add(a,b),"sub":sub(a,b),"mult":mult(a,b),"div":div(a,b)}
    toMath = math[mathing]
    return f"<h1>{toMath}</h1>"
if __name__ == "__main__":
    app.run(FLASK_ENV="environement")