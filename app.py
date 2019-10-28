from flask import Flask, jsonify, request
from flask_restful import Api, Resource, abort

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

anime = {
	1:
	{
		"name": "刀劍第三季",
		"time": "19/秋"
	},
	2:
	{
		"name": "食戟之靈 （第四季）",
		"tile": "19/秋"
	}
}

def abort_if_anime_not_found(anime_id):
	if anime_id not in anime:
		abort(404, **make_api_dict([], False, [], ['Not Found']))

class AnimeList(Resource):
	def get(self):
		return make_api_dict(anime), 200

	def post(self):
		data = request.get_json()
		li = None
		return make_api_dict(li), 200

class Anime(Resource):
	def get(self, anime_id):
		abort_if_anime_not_found(anime_id)
		return make_api_dict(anime[anime_id]), 200

api.add_resource(AnimeList, '/animes')
api.add_resource(Anime, '/animes/<int:anime_id>')

if __name__ == '__main__':
	app.run(debug=True)