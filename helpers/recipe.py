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
    """ by inheriting from dict, Ingredient objects become automatically serializable for JSON formatting """

    def __init__(self, data):
        name = data["name"]
        amount = data["amount"]["us"]["value"]
        unit = data["amount"]["us"]["unit"]

        super(Ingredient, self).__init__(name=name, amount=amount, unit=unit)

def create_objs(obj, data):
    """ create a list of desired objects """
    return [obj(row) for row in data]

def get_foods_by_name(food):
    """ get a list of all the returned foods using user provided food name """

    url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={SPOONACULAR_KEY}&query={food}&instructionsRequired=true&number=100"
    r = requests.get(url)
    food_data = json.loads(r.text)["results"]  # convert response to readable dictionary
    foods = create_objs(Food, food_data)

    return foods

def get_foods_by_ingredients(ingredients):
    """ get a list of all the returned foods using a list of user provided ingredients """

    ingredient_str = ingredients[0]
    for ingredient in ingredients[1:]:
        ingredient_str += ",+" + ingredient

    url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={SPOONACULAR_KEY}&ingredients={ingredient_str}"
    r = requests.get(url)
    food_data = json.loads(r.text)
    foods = create_objs(Food, food_data)

    return foods

def get_ingredients(food_id):
    """ get the ingredient data for a given food using its id """

    url = f"https://api.spoonacular.com/recipes/{food_id}/ingredientWidget.json?apiKey={SPOONACULAR_KEY}"
    r = requests.get(url)  # perform a get request on the url
    ingredient_data = json.loads(r.text)["ingredients"]
    ingredients = create_objs(Ingredient, ingredient_data)

    return ingredients

def get_steps(food_id):
    """ get the steps/ instructions for a given food using its id """

    url = f"https://api.spoonacular.com/recipes/{food_id}/analyzedInstructions?apiKey={SPOONACULAR_KEY}"
    r = requests.get(url)  # perform a get request on the url
    steps = json.loads(r.text)[0]["steps"]  # extract steps data from json

    return steps
