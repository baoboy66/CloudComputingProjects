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

@app.route("/historical/<date>", methods=['GET', 'DELETE'])
def getInfo(date):
    if request.method == 'GET':
        globalData = getData()
        for row in globalData:
            if row['DATE'] == date:
                return jsonify(row)
    elif request.method == 'DELETE':
        result = deleteRow(date)
        if result:
            return result
    return abort(404)


@app.route("/historical", methods=['POST'])
def addData():
    newData = request.data
    globalData.append(newData)
    return jsonify(globalData)

@app.route("/forecast/<date>", methods=['GET'])
def forecast():
    return "FORECAST DATA"
  
def getData():
    if len(globalData) > 0:
        return globalData
    import csv
    data = []
    f = open('daily.csv','rb')
    reader = csv.reader(f)
    firstLine = True
    for row in reader:
        if firstLine :
            firstLine = False
            continue
        temp = {'DATE':row[0], 'TMAX':row[1], 'TMIN':row[2]}
        data.append(temp)
    return data

def deleteRow(date)
    import csv
    data = []
    f = open('daily.csv','rb')
    reader = csv.reader(f)
    for row in reader:
        if row[0] == date:
            continue
        data.append(row)
    f.close()
    f2 = open(file.csv, 'wb')
    writer = csv.writer(f2)
    writer.writerows(data)
    f2.close
    return "Delete Successfully"
    
'''    
@app.errorHandler(404)
def not_found(error):
    return make_response(jsonify ( {'error': 'Bad Request'}),404)
'''
