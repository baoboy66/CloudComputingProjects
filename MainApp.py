from flask import Flask, request, jsonify, abort, make_response

globalData = []
app = Flask(__name__)

@app.route('/')
def main():
    return "Hello!"

@app.route("/historical", methods=['GET'])
def getDates():
    data = []
    globalData = getData()
    for row in globalData:
        temp = {'DATE':row['DATE']}
        data.append(temp)
    return jsonify(data)

@app.route("/historical/<int:date>", methods=['GET', 'DELETE'])
def getInfo(date):
    if request.method == 'GET':
        globalData = getData()
        for row in globalData:
            if row['DATE'] == date:
                return jsonify(row)
        return abort(404)
    elif request.method == 'DELETE':
        globalData = getData()
        for row in globalData:
            if row['DATE'] == date:
                globalData.remove(row)
                return "Delete Info Successful"
        return abort(404)
    return abort(404)


@app.route("/historical", methods=['POST'])
def addData():
    return "POST ADD DATA"


@app.route("/forecast/<date>", methods=['GET'])
def forecast():
    return "FORECAST DATA"
  
def getData():
    if len(globalData) > 0:
        return globalData
    import csv
    f = open('daily.csv','rb')
    reader = csv.reader(f)
    firstLine = True
    for row in reader:
        if firstLine :
            firstLine = False
            continue
        temp = {'DATE':row[0], 'TMAX':row[1], 'TMIN':row[2]}
        globalData.append(temp)
    return globalData

'''    
@app.errorHandler(404)
def not_found(error):
    return make_response(jsonify ( {'error': 'Bad Request'}),404)
'''
