import json
from flask import Flask, request, Response
app = Flask(__name__)

with open('names.json') as f:
    names = json.loads(f.read())


# what URL should trigger our function
@app.route('/')
def hello_world():
    return 'Hello!'

# you can copy/paste or type it out


@app.route('/names/<string:name>', methods=['GET'])
def get_name_meaning(name):
    return names[name.lower().capitalize()]


@app.route('/names', methods=['GET'])
def get_all_names():
    return names


@app.route('/names', methods=['POST'])
def create_name():
    data = request.json
    print(f'Adding {data} to our list of names')
    name = list(data.keys())[0]

    status = 201
    if name in names:
        status = 200

    names[name.capitalize()] = data[name]
    return Response(data, status=status, mimetype='application/json')


@app.route('/names/<name>', methods=['DELETE'])
def remove_name(name):
    print(f'Removing {name} from the list of names')
    if name in names:
        del names[name]
    return Response(status=200)
