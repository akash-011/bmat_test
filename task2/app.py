from flask import Flask, Response
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bmat_test"
mongo = PyMongo(app)


@app.route('/<iswc>')
def get_all(iswc):
	resp = mongo.db.records.find_one({"ISWC": iswc})
	res = dumps(resp['right_owners'])
	return Response(res, mimetype='application/json')


if __name__ == "__main__":
	app.run(debug=True)
