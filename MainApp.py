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
        return abort(404, {'message': 'Unable to complete request: item does not exist'})
    elif request.method == 'DELETE':
        result = deleteRow(date)
        if result:
            return result
        return abort(404, {'message': 'Unable to complete request: Cannot delete non existing item.'})


@app.route("/historical", methods=['POST'])
def addData():
    request_data = request.get_json()
    if 'DATE' in request_data:
        import csv
        data = []
        f = open('daily.csv','rb')
        reader = csv.reader(f)
        for row in reader:
            if row[0] == request_data['DATE']:
                row[1] = request_data['TMAX']
                row[2] = request_data['TMIN']
            data.append(row)
        f.close()
        f2 = open('daily.csv', 'wb')
        writer = csv.writer(f2)
        writer.writerows(data)
        f2.close
        return "Update Successfully"
    return abort(404, {'message': 'Unable to update info: item does not exist'}

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

def deleteRow(date):
    import csv
    data = []
    f = open('daily.csv','rb')
    reader = csv.reader(f)
    for row in reader:
        if row[0] == date:
            continue
        data.append(row)
    f.close()
    f2 = open('daily.csv', 'wb')
    writer = csv.writer(f2)
    writer.writerows(data)
    f2.close
    return "Delete Successfully"
    
