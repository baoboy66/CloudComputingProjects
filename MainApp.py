from flask import Flask, request, jsonify, abort, make_response

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello!"

@app.route("/historical", methods=['GET'])
def getDates():
    s = ""
    import csv
    f = open('daily.csv','rb')
    reader = csv.reader(f)
    data = []
    for row in reader:
        temp = {'DATE':row[0]}
        data.append(temp)
    return jsonify(data)

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

'''    
@app.errorHandler(404)
def not_found(error):
    return make_response(jsonify ( {'error': 'Bad Request'}),404)
'''
