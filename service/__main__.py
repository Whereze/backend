from flask import Flask, jsonify, request
import re

from service.functional.handles import new_waterfall, waterfalls #Загружаю список водопадов

app = Flask(__name__)

client = app.test_client()

@app.route("/api/v1/waterfalls/", methods = ['GET'])
def get_waterfalls():
    return jsonify(waterfalls)

@app.route("/api/v1/waterfalls/", methods = ['POST'])
def post_waterfalls():
    new_waterfall = request.json
    waterfalls.append(new_waterfall)
    return jsonify(new_waterfall)

@app.route("/api/v1/waterfalls/<int:uid>/", methods = ['GET'])
def get_uid_waterfalls(uid):
    return jsonify(waterfalls[uid])

@app.route("/api/v1/waterfalls/<int:uid>/", methods = ['PUT'])
def put_waterfalls(uid):
    changes = request.json
    waterfalls[uid].update(changes)
    return jsonify(waterfalls[uid])

@app.route("/api/v1/waterfalls/<string:key>/<string:text>/", methods = ['GET'])
def get_name_waterfalls(key,text):
    waterfall = list(filter(lambda waterfall: re.findall(text,waterfall[key], re.IGNORECASE), waterfalls))
    return jsonify(waterfall)

#TEST POST
#curl -X POST -H 'Content-Type: application/json' \ -d '{"title":"Рейнский водопад", "description": "Рейнский водопад считается самым большим равнинным водопадом в Европе"}' http://localhost:5000/
if __name__ == '__main__':
    app.run(debug=True)
