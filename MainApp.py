from flask import Flask, CSV, request

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello!"

@app.route("/historical", methods=['GET'])
def getDates():
    loadData()
    return "Dates"

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

def loadData():
    f = open('daily.csv')
    reader = csv.reader(f)
    for row in reader:
        print row
    f.close()

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 80
    )