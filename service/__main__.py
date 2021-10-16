from flask import Flask, jsonify, request, abort
from pydantic import ValidationError
import logging
import re
import orjson


from service.functional.handles import waterfalls
from service.models.db_add_method import save_waterfall_data
from service.serializers import Waterfall
from service.models.models import waterfall_details
from service.models.db import db_session
from sqlalchemy import or_

logger = logging.getLogger(__name__)

app = Flask(__name__)

client = app.test_client()


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(400)
def bad_request(e):
    return jsonify({
       'errorCode': 400,
       'massahe': "The server was unable to process the request"
    })


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500


@app.route("/api/v1/waterfalls/", methods=['GET'])
def get_waterfalls():
    query = request.args.get('q', None)
    logger.debug(query)
    waterfalls = waterfall_details.query.filter(
        or_(
            waterfall_details.title.ilike(f'%{query}%'),
            waterfall_details.summary.ilike(f'%{query}%'),
            waterfall_details.summary.ilike(f'%{query}%'),
            waterfall_details.summary.ilike(f'%{query}%'),
            waterfall_details.summary.ilike(f'%{query}%'),
            waterfall_details.summary.ilike(f'%{query}%')
    )
    return jsonify([
        Waterfall(
            uid=waterfall.uid,
            title=waterfall.title,
            description=waterfall.summary,
            height=waterfall.height,
            size=waterfall.width,
        ).dict()
        for waterfall in waterfalls
    ])

    # waterfalls = waterfall_details.query.filter(
    #     or_(
    #         waterfall_details.title.ilike("%Абай-Су%"),
    #         waterfall_details.uid > 5000
    #         # ,
    #         # waterfall_details.title == "Абай-Су")
    #     )



@app.route("/api/v1/waterfalls/", methods=['POST'])
def post_waterfalls():
    try:
        new_waterfall = request.json
        Waterfall(**new_waterfall)
        save_waterfall_data(new_waterfall)
        return jsonify(new_waterfall)
    except(ValueError, TypeError, ValidationError):
        abort(400)


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
        changes = request.json
        changes = Waterfall(**changes)
        waterfalls[uid].update(changes)
        return jsonify(waterfalls[uid])
    except ValidationError as e:
        abort(400, str(e))


# @app.route("/api/v1/waterfalls/<>/", methods=['GET'])
# def get_name_waterfalls(key, text):
#     try:
#         found_waterfalls = [
#             waterfall for waterfall in waterfalls
#             if re.findall(text, waterfall[key], re.IGNORECASE)
#         ]
#         return jsonify(found_waterfalls)

#     except(KeyError, ValueError, TypeError):
#         return 'Change key or value and try again'


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run()
