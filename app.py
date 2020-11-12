import os
from flask import (
    Flask, render_template, redirect, flash, url_for, request)
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

"""I copied most of the code above to set up flask from line 1 to 16
& the last line from the 2020 task manager mini project videos """


@app.route("/")
@app.route("/start")
def start():
    return render_template("start.html")


@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/add_recipe")
def add_recipe():
    return render_template("add_recipe.html")


@app.route("/breakfast")
def breakfast():
    categories = mongo.db.categories.find({"category": "BREAKFAST"})
    category_name = "BREAKFAST"
    return render_template(
        "category.html", categories=categories, category_name=category_name)


@app.route("/meals")
def meals():
    categories = mongo.db.categories.find({"category": "MEALS"})
    category_name = "MEALS"
    return render_template(
        "category.html", categories=categories, category_name=category_name)


@app.route("/category")
def desserts():
    categories = mongo.db.categories.find({"category": "DESSERTS"})
    category_name = mongo.db.categories.find_one({}, {"category": "DESSERTS"})
    return render_template(
        "category.html", categories=categories, category_name=category_name)


@app.route("/category")
def smoothies():
    categories = mongo.db.categories.find({"category": "SMOOTHIES"})
    category_name = mongo.db.categories.find_one({}, {"category": "SMOOTHIES"})
    return render_template(
        "category.html", categories=categories, category_name=category_name)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)