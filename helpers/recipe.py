from flask import request
import json
import requests

SPOONACULAR_KEY = "a8529c104d8749b4a19488d0fd654353"


class RecipeHandler:

    @staticmethod
    def get_ingredients(food_id):
        """ get the ingredient data for a given food using its id """

        url = f"https://api.spoonacular.com/recipes/{food_id}/ingredientWidget.json?apiKey={SPOONACULAR_KEY}"
        r = requests.get(url)  # perform a get request on the url
        ingredient_data = json.loads(r.text)["ingredients"]

        # using ingredient data, we want the name and amount of each ingredient
        ingredients = []
        for ingredient in ingredient_data:
            name = ingredient["name"]
            amount = ingredient["amount"]["us"]["value"]
            unit = ingredient["amount"]["us"]["unit"]
            ingredients.append({"name": name, "amount": amount, "unit": unit})

        return ingredients

    @staticmethod
    def get_steps(food_id):
        """ get the steps/ instructions for a given food using its id """

        url = f"https://api.spoonacular.com/recipes/{food_id}/analyzedInstructions?apiKey={SPOONACULAR_KEY}"
        r = requests.get(url)  # perform a get request on the url
        steps = json.loads(r.text)[0]["steps"]  # extract steps data from json

        return steps
