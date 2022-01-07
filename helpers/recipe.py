""" working with the spoonacular api to get food data """
import json
import requests

SPOONACULAR_KEY = "a8529c104d8749b4a19488d0fd654353"

class Food(dict):
    """ by inheriting from dict, Food objects become automatically serializable for JSON formatting """

    def __init__(self, data):
        """ create a serialized food object with desired fields """
        id = data["id"]
        name = data["title"]
        image = data["image"]

        super().__init__(self, id=id, name=name, image=image)

class Ingredient(dict):
    """ by inheriting from dict, Food objects become automatically serializable for JSON formatting """

    def __init__(self, data):
        name = data["name"]
        amount = data["amount"]["us"]["value"]
        unit = data["amount"]["us"]["unit"]

        super(Ingredient, self).__init__(name=name, amount=amount, unit=unit)

def get_foods_by_name(food):
    """ get a list of all the returned foods with their names and ids """

    url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={SPOONACULAR_KEY}&query={food}&instructionsRequired=true&number=100"
    r = requests.get(url)
    food_data = json.loads(r.text)["results"]

    # create a list of Food objects, each one containing food id, name, and image
    foods = []
    for data_row in food_data:
        foods.append(Food(data_row))

    return foods

def get_ingredients(food_id):
    """ get the ingredient data for a given food using its id """

    url = f"https://api.spoonacular.com/recipes/{food_id}/ingredientWidget.json?apiKey={SPOONACULAR_KEY}"
    r = requests.get(url)  # perform a get request on the url
    ingredient_data = json.loads(r.text)["ingredients"]

    # create a list of the desired foods Ingredient objects, each one containing ingredient name, amount, and unit
    ingredients = []
    for data_row in ingredient_data:
        ingredients.append(Ingredient(data_row))

    return ingredients

def get_steps(food_id):
    """ get the steps/ instructions for a given food using its id """

    url = f"https://api.spoonacular.com/recipes/{food_id}/analyzedInstructions?apiKey={SPOONACULAR_KEY}"
    r = requests.get(url)  # perform a get request on the url
    steps = json.loads(r.text)[0]["steps"]  # extract steps data from json

    return steps
