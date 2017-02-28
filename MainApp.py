from flask import Flask, request, jsonify, abort, make_response

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello!"

@app.route("/historical", methods=['GET'])
def getDates():
    import csv
    f = open('daily.csv','rb')
    reader = csv.reader(f)
    data = []
    firstLine = True
    for row in reader:
        if firstLine :
            firstLine = False
            continue
        temp = {'DATE':row[0]}
        data.append(temp)
    return jsonify(data)

@app.route("/historical/<date>", methods=['GET', 'DELETE'])
def getInfo(date):
    if request.method == 'GET':
        data = getData()
        for i in data:
            if i[0] == date:
                return ['DATE':i[0], 'TMAX':i[1], 'TMIN':i[2]]
    elif request.method == 'DELETE':
        return "Delete Info"
    return "NONE"


@app.route("/historical", methods=['POST'])
def addData():
    return "POST ADD DATA"


@app.route("/forecast/<date>", methods=['GET'])
def forecast():
    return "FORECAST DATA"

def getData():
        import csv
    f = open('daily.csv','rb')
    reader = csv.reader(f)
    data = []
    firstLine = True
    for row in reader:
        if firstLine :
            firstLine = False
            continue
        data.append(row)
    return data
    
'''    
@app.errorHandler(404)
def not_found(error):
    return make_response(jsonify ( {'error': 'Bad Request'}),404)
'''
