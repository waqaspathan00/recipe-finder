""" controls post and get requests relating to recipes """

from flask import render_template, request
from helpers.recipe import RecipeHandler

SPOONACULAR_KEY = "a8529c104d8749b4a19488d0fd654353"

class RecipeController:

    @staticmethod
    def post():
        if request.method == "POST":
            """ 
            when the user submits a food name, create a list of all the related food names and ids 
            
            for right now we will only return data for the first food
            """

            food = request.form.get("food")

            # get a list of all the food results for the user searched food
            foods = RecipeHandler.get_foods(food)
            print(foods)
            # Writer.write_line("website/data.csv", data)

            # # get ingredients for the first food
            # ingredients = RecipeHandler.get_ingredients(foods[0]["id"])
            #
            # # get steps for the first food
            # steps = RecipeHandler.get_steps(foods[0]["id"])

            return render_template("home.html", foods=foods)
        return render_template("home.html")

    @staticmethod
    def get():
        pass
