""" this file manages our different views """

from flask import Blueprint, render_template, request
import requests

views = Blueprint("views", __name__)
SPOONACULAR_KEY = "a8529c104d8749b4a19488d0fd654353"

@views.route("/")
def home():
    """ the default path is to home.html """
    # passing a variable named text to home.html
    return render_template("home.html")

@views.route("/", methods=["POST"])
def send_recipe():
    if request.method == "POST":
        food = request.form.get("food")

        # get the name and id of a food relevant to what the user searched for
        url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={SPOONACULAR_KEY}&query={food}&instructionsRequired=true"
        r = requests.get(url)
        food_data = eval(r.text)["results"]
        food_name = food_data[0]["title"]

        return render_template("home.html", food_name=food_name)
    return render_template("home.html")
