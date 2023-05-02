from flask import Flask, request, render_template, jsonify, redirect
from pymongo import MongoClient
from bson import ObjectId


app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/nargiza')
db = client['config_db']
collection = db['config_collection']


@app.route("/upload", methods=["POST"])
def upload_config():
    config_data = request.get_json()
    if not config_data:
        return jsonify({"error": "invalid data"}), 400
    try:
        config_id = collection.insert_one(config_data).inserted_id
        return redirect("/", code=302)
    except Exception as e:
        print(e)
        return jsonify({"error": "failed to save"}), 500

@app.route("/")
def index():
    configs = collection.find()
    return render_template("index.html", configs=configs)

@app.route("/configs", methods=["GET"])
def config_list():
    configs = collection.find()
    return render_template("configs.html", configs=configs)

@app.route("/configs/<config_id>", methods=["GET", "DELETE"])
def get_config(config_id):
    if request.method == "DELETE":
        result = collection.delete_one({"_id": ObjectId(config_id)})
        if result.deleted_count > 0:
            return jsonify({"success": "config deleted"}), 200
        else:
            return jsonify({"error": "config not found"}), 404
    else:
        config = collection.find_one({"_id": ObjectId(config_id)})
        if config:
            return render_template("config.html", config=config)
        else:
            return jsonify({"error": "config not found"}), 404


if __name__ == '__main__':
   app.run(debug=True)


