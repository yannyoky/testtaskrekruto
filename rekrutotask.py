import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    try:
        return 'hello world'
    except KeyError:
        return f'Invalid input'
