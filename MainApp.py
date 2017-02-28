from flask import Flask, request, csv

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello!"

@app.route("/historical", methods=['GET'])
def getDates():
    s = ""
    f = open('daily.csv','rb')
    reader = csv.reader(f)
    for row in reader:
        s += str(row)
    return s

@app.route("/historical/<date>", methods=['GET', 'DELETE'])
def getInfo():
    if request.method == 'GET':
        return "Get Info"
    elif request.method == 'DELETE':
        return "Delete Info"
    return "NONE"


@app.route("/historical", methods=['POST'])
def addData():
    return "POST ADD DATA"


@app.route("/forecast/<date>", methods=['GET'])
def forecast():
    return "FORECAST DATA"

