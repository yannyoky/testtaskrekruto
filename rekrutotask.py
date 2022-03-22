from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_strings():
    name = request.args['name']
    message = request.args['message']
    return '''<h1>{}</h1><h1>{}</h1>'''.format(name, message)
if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/?name=Rekruto&message=Давай дружить!