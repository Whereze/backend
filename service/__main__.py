from flask import Flask, jsonify, request, abort
from pydantic import ValidationError
from typing import Optional
import re
from pydantic.main import BaseModel
from service.functional.handles import waterfalls
from service.functional.waterfalls_basemodel import Waterfall_model

app = Flask(__name__)

client = app.test_client()


class Waterfall(BaseModel):
    uid: Optional[int]
    title: Optional[str]
    description: Optional[str]
    height: Optional[int]
    size: Optional[int]


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(400)
def internal_server_error(e):
    return jsonify(error=str(e)), 400


@app.route("/api/v1/waterfalls/", methods=['GET'])
def get_waterfalls():
    try:
        if waterfalls:
            return jsonify(waterfalls)
        else:
            return 'No waterfalls yet'
    except(ValueError, TypeError):
        return 'Change your request'


@app.route("/api/v1/waterfalls/", methods=['POST'])
def post_waterfalls():
    try:
        new_waterfall = request.json
        waterfalls.append(new_waterfall)
        return jsonify(new_waterfall)
    except(ValueError, TypeError):
        return 'Change your request'


@app.route("/api/v1/waterfalls/<int:uid>/", methods=['GET'])
def get_uid_waterfalls(uid):
    try:
        waterfall = waterfalls[uid]
        if waterfall is None:
            abort(404, description="Resource not found")
        return jsonify(waterfalls[uid])
    except(KeyError, ValueError, TypeError, IndexError):
        return 'Change your request'


@app.route("/api/v1/waterfalls/<int:uid>/", methods=['PUT'])
def put_waterfalls(uid):
    try:
        try:
            changes = request.json
            changes = Waterfall_model(**changes)
            waterfalls[uid].update(changes)
            return jsonify(waterfalls[uid])
        except ValidationError as e:
            return e.json()
    except(KeyError, ValueError, TypeError, IndexError):
        return 'Change your request'


@app.route("/api/v1/waterfalls/<string:key>/<string:text>/", methods=['GET'])
def get_name_waterfalls(key, text):
    try:
        found_waterfalls = [
            waterfall for waterfall in waterfalls
            if re.findall(text, waterfall[key], re.IGNORECASE)
        ]
        return jsonify(found_waterfalls)

    except(KeyError, ValueError, TypeError):
        return 'Change key or value and try again'


if __name__ == '__main__':
    app.run(debug=True)
