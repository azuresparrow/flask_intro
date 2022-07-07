from flask import Flask
from flask import request
import operations

app = Flask(__name__)

@app.route("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.add(a,b))
    
@app.route("/sub")
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.sub(a,b))

@app.route("/mult")
def mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.mult(a,b))

@app.route("/div")
def div():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return str(operations.div(a,b))

@app.route("/math/<operator>")
def math(operator):
    a = float(request.args["a"])
    b = float(request.args["b"])
    if (operator == "add"): result = operations.add(a,b)
    elif (operator == "sub"): result = operations.sub(a,b)
    elif (operator == "mult"): result = operations.mult(a,b)
    elif (operator == "div"): result = operations.div(a,b)
    
    return str(result)
