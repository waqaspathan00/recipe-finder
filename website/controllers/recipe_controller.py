""" controls post and get requests relating to recipes """

from flask import render_template, request, session
from helpers.recipe import get_foods, get_ingredients, get_steps

class RecipeController:
    """ handle get and post requests concerning food recipes on homepage """

    @staticmethod
    def post():
        """
        when the user submits a food name, create a list of all the related food names and ids

        for right now we will only return data for the first food
        """
        if request.method == "POST":
            # get the food entered by user
            food = request.form.get("food")

            # store food data in session for use by GET
            foods = get_foods(food)
            session["foods"] = foods

            return render_template("home.html", foods=foods)
        return render_template("home.html")

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
