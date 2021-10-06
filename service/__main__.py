from flask import Flask, jsonify, request
import re

from service.functional.handles import waterfalls

app = Flask(__name__)


client = app.test_client()


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'errorCode': 404,
        'message': "Woops, that page doesn't exist!",
    })


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'errorCode': 500, 'message': "Internal server mistake :("})


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
        if waterfall:
            return jsonify(waterfalls[uid])
        else:
            return 'Waterfall not found'
    except(KeyError, ValueError, TypeError, IndexError):
        return 'Change your request'


@app.route("/api/v1/waterfalls/<int:uid>/", methods=['PUT'])
def put_waterfalls(uid):
    try:
        changes = request.json
        waterfalls[uid].update(changes)
        return jsonify(waterfalls[uid])
    except(KeyError, ValueError, TypeError, IndexError):
        return 'Change your request'


@app.route("/api/v1/waterfalls/<string:key>/<string:text>/", methods=['GET'])
def get_name_waterfalls(key, text):
    try:
        found_waterfalls = [
            waterfall for waterfall in waterfalls
            if re.findall(text, waterfall[key], re.re.IGNORECASE)
        ]
        return jsonify(found_waterfalls)

    except(KeyError, ValueError, TypeError):
        return 'Change key or value and try again'


if __name__ == '__main__':
    app.run(debug=True)
