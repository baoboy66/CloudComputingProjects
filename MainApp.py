from flask import Flask, request, jsonify, abort, make_response

globalData = []
app = Flask(__name__)

@app.route('/')
def main():
    return "Hello!"

@app.route("/historical/", methods=['GET'])
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
            return result, 204
        return abort(404, {'message': 'Unable to complete request: Cannot delete non existing item.'})


@app.route("/historical/", methods=['POST'])
def addData():
    request_data = request.get_json()
    try:
        import csv
        data = []
        f = open('daily.csv','rb')
        reader = csv.reader(f)
        found = False
        for row in reader:
            if row[0] == request_data['DATE']:
                temp = [request_data['DATE'],request_data['TMAX'],request_data['TMIN']]
                data.append(temp)
                found = True
            else:
                data.append(row)
        if not found:
            temp = [request_data['DATE'],request_data['TMAX'],request_data['TMIN']]
            data.append(temp)
        f.close()
        f2 = open('daily.csv', 'wb')
        writer = csv.writer(f2)
        writer.writerows(data)
        f2.close()
        result = {'DATE':request_data['DATE']}
        return make_response(jsonify(result),201)
    except:
        return abort(404, {'message': 'Unable to update info: item does not exist'})

@app.route("/forecast/<date_id>", methods=['GET'])
def forecast(date_id):
    # get the forecast for existing dates
    globalData = getData()
    data = []
    count = 0
    flag = False
    for row in globalData:
        if row['DATE'] == date_id:
            flag = True
        if flag and count < 7:
            data.append(row)
            count += 1
    if len(data) > 0:
        return jsonify(data)
    return abort(404, {'Message':'No data found for the next 7 days'})
  
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
    
