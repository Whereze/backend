from flask import Flask, jsonify, request, abort, make_response
from pydantic import ValidationError
import logging
from service.serializers import WaterfallModel
from service.waterfalls import WaterfallRepo

logger = logging.getLogger(__name__)

app = Flask(__name__)

client = app.test_client()

repo = WaterfallRepo()


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
    try:
        title = request.args.get('title', None)
        detail = request.args.get('detail', None)
        waterfalls = repo.get(title, detail)
        return jsonify([
            WaterfallModel(
                    uid=waterfall.uid,
                    title=waterfall.title,
                    summary=waterfall.summary,
                    height=waterfall.height,
                    width=waterfall.width,
                    river=waterfall.river,
                    country=waterfall.country,
                    region=waterfall.region,
                    RF_subject=waterfall.RF_subject,
            ).dict()
            for waterfall in waterfalls
        ])
    except ValidationError as e:
        abort(400, str(e))


@app.route("/api/v1/waterfalls/", methods=['POST'])
def post_waterfalls():
    try:
        new_waterfall = request.json
        WaterfallModel(**new_waterfall)
        new_waterfall = repo.add(
                                title=new_waterfall['title'],
                                summary=new_waterfall['summary'],
                                height=new_waterfall['height'],
                                width=new_waterfall['width'],
                                river=new_waterfall['river'],
                                country=new_waterfall['country'],
                                region=new_waterfall['region'],
                                RF_subject=new_waterfall['RF_subject']
                                )
        return jsonify(new_waterfall.title, new_waterfall.summary)
    except(ValueError, TypeError, ValidationError):
        abort(400)


@app.route("/api/v1/waterfalls/<int:uid>/", methods=['PUT'])
def put_waterfalls(uid):
    try:
        changes = request.json
        WaterfallModel(**changes)
        if not repo.check_by_id(uid):
            abort(make_response(jsonify(
                f"Waterfall with id {uid} doesn\'t exist."), 400))
        else:
            waterfall = repo.update(
                                    uid=uid,
                                    title=changes['title'],
                                    summary=changes['summary'],
                                    height=changes['height'],
                                    width=changes['width'],
                                    river=changes['river'],
                                    country=changes['country'],
                                    region=changes['region'],
                                    RF_subject=changes['RF_subject']
                            )

        return jsonify(waterfall.title, waterfall.summary)
    except ValidationError as e:
        abort(400, str(e))


@app.route("/api/v1/waterfalls/<int:uid>/", methods=['DELETE'])
def delete_waterfalls(uid):
    try:
        if not repo.check_by_id(uid):
            abort(make_response(jsonify(
                f"Waterfall with id {uid} doesn\'t exist."), 400))
        repo.delete(uid)
        return jsonify(f"Waterfall with id {uid} was deleted")
    except ValidationError as e:
        abort(400, str(e))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run()
