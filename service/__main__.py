from flask import Flask
from service.functional.handles import *

app = Flask(__name__)
@app.route("/")
def uid_waterlall():
    new_waterfall('Рейнский водопад', 'Рейнский водопад считается самым большим равнинным водопадом в Европе',
    150, 23)
    waterfall = take_uid_waterfall(2)
    return waterfall

if __name__ == '__main__':
    app.run(debug=True)