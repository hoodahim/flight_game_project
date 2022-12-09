# Connects the python with JavaScript.
# Calls function airport_fetcher based on player's choice of ICAO code.
# airport_fetcher return the data to JavaScript.

from flask import Flask, request
from flask_cors import CORS
from airport_fetcher import airport_fetcher

app = Flask(__name__)
cors = CORS(app)


# http://127.0.0.1:5000/new_game?loc=EFHK
@app.route('/new_game')
def new_game():
    args = request.args
    location = args.get("loc")
    json_data = airport_fetcher(location)
    return json_data


# http://127.0.0.1:5000/fly_to?new_loc=EGLL
@app.route('/fly_to')
def fly_to():
    args = request.args
    new_location = args.get("new_loc")
    json_data = airport_fetcher(new_location)
    return json_data


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
