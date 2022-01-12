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
        when the user submits a food name
        create a list of all the related food names and ids

        :return: to home page with either nothing or the food results
        """
        if request.method == "POST":
            # get the food entered by user
            food = request.form.get("food")

            url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={SPOONACULAR_KEY}&query={food}&instructionsRequired=true&number=100"
            r = requests.get(url)
            if r.status_code == 402:  # 402 - payment required (to spoonacular for more API calls)
                flash("Currently out of API calls. Try again later.", category="error")
                return render_template("home.html")

            food_data = json.loads(r.text)["results"]
            if not food_data:  # checking if food_data is empty
                flash("No results found.", category="warning")
                return render_template("home.html")

            # store food data in session for use by GET
            foods = get_foods(food_data)
            session["foods"] = foods

            return render_template("home.html", foods=foods)
        return render_template("home.html")

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

            url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={SPOONACULAR_KEY}&ingredients={ingredient_str}"
            r = requests.get(url)
            if r.status_code == 402:
                flash("Sorry, currently out of API calls. Try again later.", category="error")
                return render_template("fridge.html")

            food_data = json.loads(r.text)

            # store food data in session for use by GET
            foods = get_foods(food_data)
            session["foods"] = foods

            return render_template("fridge.html", foods=foods)
        return render_template("fridge.html")

    @staticmethod
    def get():
        """ getting the ingredients and steps for a clicked food """

        # get the data of the food clicked by user from session
        food = eval(request.args['type'])
        name = food["name"]
        image = food["image"]

        # get ingredients for the food
        url = f"https://api.spoonacular.com/recipes/{food['id']}/ingredientWidget.json?apiKey={SPOONACULAR_KEY}"
        r = requests.get(url)  # perform a get request on the url
        data = json.loads(r.text)["ingredients"]
        ingredients = get_ingredients(data)

        # get steps for the food
        url = f"https://api.spoonacular.com/recipes/{food['id']}/analyzedInstructions?apiKey={SPOONACULAR_KEY}"
        r = requests.get(url)  # perform a get request on the url
        data = json.loads(r.text)[0]["steps"]  # extract steps data from json
        steps = get_steps(data)

        return render_template("recipe.html", name=name, image=image, ingredients=ingredients, steps=steps)
