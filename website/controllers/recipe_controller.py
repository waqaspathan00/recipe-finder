""" controls post and get requests relating to recipes """

from flask import render_template, request
from helpers.csv_handler import Writer
from helpers.recipe import RecipeHandler
import requests
import json

SPOONACULAR_KEY = "a8529c104d8749b4a19488d0fd654353"

class RecipeController:

    @staticmethod
    def post():
        if request.method == "POST":
            """ 
            when the user makes a request, store data in data.csv containing the names and ids of all the foods in the list
            then if and when the user hits one of the arrow keys to see the next result
                it will access the list of results and call data for them respectively as seen fit

            the initial POST request must return a list of all the results AND the ingredients and steps for the first result
            """

            food = request.form.get("food")

            # get the name and id of a food relevant to what the user searched for
            url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={SPOONACULAR_KEY}&query={food}&instructionsRequired=true"
            r = requests.get(url)
            food_data = json.loads(r.text)["results"]
            first_food_name = food_data[0]["title"]
            first_food_id = food_data[0]["id"]

            # get the ingredient data for the extracted recipe
            url = f"https://api.spoonacular.com/recipes/{food_id}/ingredientWidget.json?apiKey={SPOONACULAR_KEY}"
            r = requests.get(url)
            ingredient_data = json.loads(r.text)["ingredients"]

            ingredients = RecipeHandler.get_ingredients(first_food_id)

            steps = RecipeHandler.get_steps(first_food_id)

            return render_template("home.html", first_food_name=first_food_name, ingredients=ingredients, steps=steps)
        return render_template("home.html")

    @staticmethod
    def get():
        pass
