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


@app.route("/recipes/<id_for_recipe>")
def recipes(id_for_recipe):
    recipe = mongo.db.recipes.find_one({"_id":  ObjectId(id_for_recipe)})
    print(recipe)
    print(id_for_recipe)
    return render_template("recipe._detail.html", recipe=recipe)


@app.route("/breakfast")
def breakfast():
    categories = mongo.db.recipes.find({"category": "BREAKFAST"})
    category_name = "BREAKFAST"
    return render_template(
        "category.html", categories=categories, category_name=category_name)


@app.route("/meals")
def meals():
    categories = mongo.db.recipes.find({"category": "MEALS"})
    category_name = "MEALS"
    return render_template(
        "category.html", categories=categories, category_name=category_name)


@app.route("/desserts")
def desserts():
    categories = mongo.db.recipes.find({"category": "DESSERTS"})
    category_name = "DESSERTS"
    return render_template(
        "category.html", categories=categories, category_name=category_name)


@app.route("/smoothies")
def smoothies():
    categories = mongo.db.recipes.find({"category": "SMOOTHIES"})
    category_name = "SMOOTHIES"
    return render_template(
        "category.html", categories=categories, category_name=category_name)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        added_recipe = {
            "category": request.form.get("category"),
            "image": request.form.get("image"),
            "time": request.form.get("time"),
            "portions": request.form.get("portions"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients": request.form.getlist("ingredients"),
            "instructions": request.form.getlist("ingredients"),
            "added_by": request.form.getlist("added_by")
        }
        mongo.db.recipes.insert_one(added_recipe)
        flash("Recipe Successfully Added")

    return render_template("add_recipe.html")


@app.route("/my_recipes")
def my_recipes():
    return render_template("my_recipes.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)