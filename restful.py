from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

devs = [
    {'nome': 'Andre',
     'habilidades': ['python', 'flask', 'react', 'node', 'typescript', 'javascript']},
    {'nome': 'Rafael',
     'habilidades': ['python', 'flask', 'django']}
]


class DevByID(Resource):
    @staticmethod
    def get(_id):
        try:
            dev = devs[_id]
            return dev
        except IndexError:
            return {'status': 'error', 'mensagem': f'no entry for id {_id}'}
        except Exception:
            return {'status': 'erro', 'mensagem': 'unknown error'}

    @staticmethod
    def put(_id):
        try:
            new_info = json.loads(request.data)
            devs[_id] = new_info
            return devs
        except IndexError:
            return {'status': 'error', 'mensagem': f'no entry for id {_id}'}
        except Exception:
            return {'status': 'erro', 'mensagem': 'unknown error'}

    @staticmethod
    def delete(_id):
        try:
            devs.pop(_id)
            return devs
        except IndexError:
            return {'status': 'error', 'mensagem': f'no entry for id {_id}'}
        except Exception:
            return {'status': 'erro', 'mensagem': 'unknown error'}


api.add_resource(DevByID, '/dev/<int:_id>')


class Dev(Resource):
    @staticmethod
    def get():
        return devs

    @staticmethod
    def post():
        new_dev = json.loads(request.data)
        devs.append(new_dev)
        return new_dev


api.add_resource(Dev, '/dev')


if __name__ == '__main__':
    app.run(debug=True)
