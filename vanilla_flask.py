import json
from flask import Flask, jsonify, request

app = Flask(__name__)


devs = [
    {'nome': 'Andre',
     'habilidades': ['python', 'flask', 'react', 'node', 'typescript', 'javascript']},
    {'nome': 'Rafael',
     'habilidades': ['python', 'flask', 'django']}
]


@app.get('/dev/<int:_id>')
def get_dev(_id):
    try:
        dev = devs[_id]
        return dev
    except IndexError:
        return {'status': 'error', 'mensagem': f'no entry for id {_id}'}
    except Exception:
        return jsonify({'status': 'erro', 'mensagem': 'unknown error'})


@app.put('/dev/<int:_id>')
def put_dev(_id):
    try:
        new_info = json.loads(request.data)
        devs[_id] = new_info
        return devs
    except IndexError:
        return {'status': 'error', 'mensagem': f'no entry for id {_id}'}
    except Exception:
        return jsonify({'status': 'erro', 'mensagem': 'unknown error'})


@app.delete('/dev/<int:_id>')
def delete_dev(_id):
    try:
        devs.pop(_id)
        return devs
    except IndexError:
        return {'status': 'error', 'mensagem': f'no entry for id {_id}'}
    except Exception:
        return jsonify({'status': 'erro', 'mensagem': 'unknown error'})


@app.get('/dev')
def get_all_devs():
    return devs


@app.post('/dev')
def post_dev():
    new_dev = json.loads(request.data)
    devs.append(new_dev)
    return devs


if __name__ == '__main__':
    app.run(debug=True)
