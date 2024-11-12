from flask import Flask, render_template 
from .posts import posts

app = Flask(__name__)


@app.route("/")
def index():
    # return render_template("index.html")
    return "<h1>Hello there! </h1>"


@app.route("/posts/all")
def get_all_users():
    print(posts)
    return render_template("feed.html", posts=posts)
    return {"posts": posts, "users": "Tom" }


@app.route("/posts/<int:id>")
def get_one_post(id):
    print(id)
    one_post = [ post for post in posts if post["id"] == id]
    print(one_post)
    return render_template("feed.html", posts=one_post)