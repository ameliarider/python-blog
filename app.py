from flask import Flask, request
from flask_cors import CORS
import db

app = Flask(__name__)
cors = CORS(app, resources={"/*": {"origins": "http://localhost:5173", "supports_credentials": True}})


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/posts.json")
def index():
    return db.posts_all()

@app.route("/posts.json", methods=["POST"])
def create():
    if request.is_json:
        data = request.json
    else:
        data = request.form
    title = data.get("title")
    content = data.get("content")
    return db.posts_create(title, content)

@app.route("/posts/<id>.json")
def show(id):
    return db.posts_find_by_id(id)

@app.route("/posts/<id>.json", methods=["PATCH"])
def update(id):
    if request.is_json:
        data = request.json
    else:
        data = request.form
    post = db.posts_find_by_id(id)
    title = data.get("title") or post["title"]
    content = data.get("content") or post["content"]
    return db.posts_update_by_id(id, title, content)