""" this file manages our different views """
from pprint import pprint
from flask import Blueprint, render_template, request
import requests
import json

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
        # food_data = eval(r.text)["results"]
        food_data = json.loads(r.text)["results"]
        food_name = food_data[0]["title"]
        food_id = food_data[0]["id"]

        # get the ingredient data for the extracted recipe
        url = f"https://api.spoonacular.com/recipes/{food_id}/ingredientWidget.json?apiKey={SPOONACULAR_KEY}"
        r = requests.get(url)
        ingredient_data = json.loads(r.text)["ingredients"]

        # using ingredient data, we want the name and amount of each ingredient
        ingredients = []
        for ingredient in ingredient_data:
            name = ingredient["name"]
            amount = ingredient["amount"]["us"]
            ingredients.append([name, amount])

        url = f"https://api.spoonacular.com/recipes/{food_id}/analyzedInstructions?apiKey={SPOONACULAR_KEY}"
        r = requests.get(url)

        steps = json.loads(r.text)[0]["steps"]
        pprint(steps)

        return render_template("home.html", food_name=food_name, ingredient_data=ingredient_data, steps=steps)
    return render_template("home.html")
