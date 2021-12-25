""" working with the spoonacular api to get food data """
import json
import requests

SPOONACULAR_KEY = "a8529c104d8749b4a19488d0fd654353"

def get_foods(food):
    """ get a list of all the returned foods with their names and ids """

    url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={SPOONACULAR_KEY}&query={food}&instructionsRequired=true"
    r = requests.get(url)
    food_data = json.loads(r.text)["results"]

    print(food_data)

    foods = []
    for row in food_data:
        food_name = row["title"]
        food_id = row["id"]
        food_image = row["image"]
        foods.append({"name": food_name, "id": food_id, "image": food_image})

    return foods

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

def get_steps(food_id):
    """ get the steps/ instructions for a given food using its id """

    url = f"https://api.spoonacular.com/recipes/{food_id}/analyzedInstructions?apiKey={SPOONACULAR_KEY}"
    r = requests.get(url)  # perform a get request on the url
    steps = json.loads(r.text)[0]["steps"]  # extract steps data from json

    return steps
