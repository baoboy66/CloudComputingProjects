from flask import Flask, #request, CSV

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello!"

@app.route("/historical", methods=['GET'])
def getDates():
    return "Dates"

@app.route("historical/<date>", methods=['GET'])
def getInfo():
    return "GET INFO";


@app.route("/historical", methods=['POST'])
def addData():
    return "POST ADD DATA";

@app.route("historical/<date>", methods=['DELETE'])
def deleteData():
    return "DELETE DATA"

@app.route("forecast/<date>", methods=['GET'])
def forecast():
    return "FORECAST DATA"

def loadData():
    f = open('daily.csv')
    #csv.reader(f)
    f.close()