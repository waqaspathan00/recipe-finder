""" controls post and get requests relating to recipes """

from flask import render_template, request, session, flash
import requests, json
from helpers.recipe import get_foods, get_ingredients, get_steps

SPOONACULAR_KEY = "a8529c104d8749b4a19488d0fd654353"

class RecipeController:
    """ handle get and post requests concerning food recipes on homepage """

    @staticmethod
    def post_name():
        """
        when the user submits a food name, create a list of all the related food names and ids

        for right now we will only return data for the first food
        """
        if request.method == "POST":
            # get the food entered by user
            food = request.form.get("food")

            url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={SPOONACULAR_KEY}&query={food}&instructionsRequired=true&number=100"
            r = requests.get(url)
            if r.status_code == 402:
                flash("Sorry, currently out of API calls. Try again later.", category="error")
                return render_template("home.html")

            food_data = json.loads(r.text)["results"]

            # store food data in session for use by GET
            foods = get_foods(food_data)
            session["foods"] = foods

            return render_template("home.html", foods=foods)
        return render_template("home.html")

    @staticmethod
    def post_ingredients():
        if request.method == "POST":
            # get the food entered by user
            ingredients = request.form.getlist("ingredients[]")

            ingredient_str = ingredients[0]
            for ingredient in ingredients[1:]:
                ingredient_str += ",+" + ingredient

            url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={SPOONACULAR_KEY}&ingredients={ingredient_str}"
            r = requests.get(url)
            if r.status_code == 402:
                flash("Sorry, currently out of API calls. Try again later.", category="error")
                return render_template("home.html")

            food_data = json.loads(r.text)

            # store food data in session for use by GET
            foods = get_foods(food_data)
            # session["foods"] = foods

            return render_template("fridge.html", foods=foods)
        return render_template("fridge.html")

    @staticmethod
    def get():
        """ getting the ingredients and steps for a clicked food """

        # get the data of the food clicked by user from session
        food = eval(request.args['type'])
        name = food["name"]
        image = food["image"]

        # get ingredients for the first food
        ingredients = get_ingredients(food["id"])

        # get steps for the first food
        steps = get_steps(food["id"])
        return render_template("recipe.html", name=name, image=image, ingredients=ingredients, steps=steps)
