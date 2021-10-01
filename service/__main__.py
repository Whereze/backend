from flask import Flask, jsonify, request

from service.functional.handles import waterfalls #Загружаю список водопадов

app = Flask(__name__)

client = app.test_client()

@app.route("/", methods = ['GET'])
def get_waterfalls():
    return jsonify(waterfalls)

@app.route("/", methods = ['POST'])
def post_waterfalls():
    new_waterfall = request.json
    waterfalls.append(new_waterfall)
    return jsonify(waterfalls)

if __name__ == '__main__':
    app.run(debug=True)