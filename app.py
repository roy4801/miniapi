from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def make_api_error(code, msg):
	return {'code': code,
			'message': msg}

def make_api_dict(results, status=True, message=[], errors=[]):
	res = {'results': results,
		   'status': status,
		   'message': message,
		   'errors': errors}
	return res

def make_api_response(results, status=True, message=[], errors=[]):
	response = jsonify(make_api_dict(results, status, message, errors))
	return response

class HelloWorld(Resource):
	def get(self):
		return make_api_dict([], False), 200

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
	app.run(debug=True)