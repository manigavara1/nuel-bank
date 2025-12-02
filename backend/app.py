from flask import Flask
from pymongo import MongoClient
import os

app = Flask(_name_)

mongo_url = os.environ.get("MONGO_URL", "mongodb://mongo:27017/")
client = MongoClient(mongo_url)
db = client["nuelbank"]

@app.route("/")
def home():
    return "✅ NUEL BANK APPLICATION IS RUNNING SUCCESSFULLY!"

@app.route("/health")
def health():
    return {"status": "OK", "service": "Nuel Bank"}

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000, debug=True)
