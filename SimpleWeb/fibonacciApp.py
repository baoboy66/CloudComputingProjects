
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return open('input_form.html','r').read()

@app.route("/echo", methods=['POST'])
def echo():
    input = int(request.form['number'])
    result = fib(input)
    return "Fibonacci Number is : " + str(result)

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
