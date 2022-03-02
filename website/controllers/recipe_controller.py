""" controls post and get requests relating to recipes """

import json
import requests
from flask import render_template, request, session, flash
from helpers.recipe import get_foods, get_ingredients, get_steps\

SPOONACULAR_KEY = "a8529c104d8749b4a19488d0fd654353"

class RecipeController:
    """ handle get and post requests concerning food recipes on homepage """

    @staticmethod
    def post_name():
        """
        when the user submits a food name
        create a list of all the related food names and ids

        :return: to index page with either nothing or the food results
        """
        if request.method == "POST":
            # get the food entered by user
            food = request.form.get("food")

            url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={SPOONACULAR_KEY}" \
                  f"&query={food}&instructionsRequired=true&number=100"
            response = requests.get(url)

            # 402 - payment required (to spoonacular for more API calls)
            if response.status_code == 402:
                flash("Currently out of API calls. Try again later.", category="error")
                return render_template("index.html")

            food_data = json.loads(response.text)["results"]
            if not food_data:  # checking if food_data is empty
                flash("No results found.", category="warning")
                return render_template("index.html")

            # store food data in session for use by GET
            foods = get_foods(food_data)
            # session["foods"] = foods

            return render_template("index.html", foods=foods)
        return render_template("index.html")

    @staticmethod
    def post_ingredients():
        """
        when the user submits a list of ingredients
        create a list of all the related foods that contain those ingredients

        :return: to fridge page with either nothing or the food results
        """
        if request.method == "POST":
            # get the food entered by user
            ingredients = request.form.getlist("ingredients[]")

            ingredient_str = ingredients[0]
            for ingredient in ingredients[1:]:
                ingredient_str += ",+" + ingredient

            url = f"https://api.spoonacular.com/recipes/findByIngredients" \
                  f"?apiKey={SPOONACULAR_KEY}&ingredients={ingredient_str}"

            response = requests.get(url)
            if response.status_code == 402:
                flash("Sorry, currently out of API calls. Try again later.", category="error")
                return render_template("fridge.html")

            food_data = json.loads(response.text)

            # store food data in session for use by GET
            foods = get_foods(food_data)
            session["foods"] = foods

            return render_template("fridge.html", foods=foods)
        return render_template("fridge.html")

    @staticmethod
    def get():
        """ getting the ingredients and steps for a clicked food """

        # get the data of the food clicked by user from session
        # pylint: disable=W0123
        food = eval(request.args["type"])
        name = food["name"]
        image = food["image"]

        # get ingredients for the food
        url = f"https://api.spoonacular.com/recipes/{food['id']}/ingredientWidget.json" \
              f"?apiKey={SPOONACULAR_KEY}"
        response = requests.get(url)  # perform a get request on the url
        data = json.loads(response.text)["ingredients"]
        ingredients = get_ingredients(data)

        # get steps for the food
        url = f"https://api.spoonacular.com/recipes/{food['id']}/analyzedInstructions" \
              f"?apiKey={SPOONACULAR_KEY}"
        response = requests.get(url)  # perform a get request on the url
        data = json.loads(response.text)[0]["steps"]  # extract steps data from json
        steps = get_steps(data)

        return render_template("recipe.html",
                               name=name, image=image, ingredients=ingredients, steps=steps)
