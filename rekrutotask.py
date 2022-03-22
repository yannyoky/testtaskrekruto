from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    try:
        name = request.args['name']
        message = request.args['message']
        return '''<h1>{}</h1><h1>{}</h1>'''.format(name, message)
    except:
        name = 'Rekruto'
        message = 'Давай дружить'
        return '''<h1>{}</h1><h1>{}</h1>'''.format(name, message)
