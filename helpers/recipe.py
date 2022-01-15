""" working with the spoonacular api to get food data """
from .models import Food, Ingredient, Step

SPOONACULAR_KEY = "a8529c104d8749b4a19488d0fd654353"

def create_objs(obj, data):
    """ create a list of desired objects """
    return [obj(row) for row in data]

def get_foods(data):
    """
    get a list of food results using the data provided

    [
        {
            'id': 665769,
            'title': 'Zucchini Pizza Boats',
            'image': 'https://spoonacular.com/recipeImages/665769-312x231.jpg',
        },
        {
            'id': 655847,
            'title': 'Pesto Veggie Pizza',
            'image': 'https://spoonacular.com/recipeImages/655847-312x231.jpg',
        }
    ]
    """
    print(data)
    return create_objs(Food, data)

def get_ingredients(data):
    """
    get the ingredient data for a given food using its id

    EXAMPLE DATA
    [
        {
            'name': 'olive oil',
            'image': 'olive-oil.jpg',
            'amount': {
                'metric': {'value': 1.0, 'unit': 'serving'},
                'us': {'value': 1.0, 'unit': 'serving'}
            }
        },
        {
            'name': 'sea salt',
            'image': 'salt.jpg',
            'amount': {
                'metric': {'value': 1.0, 'unit': 'serving'},
                'us': {'value': 1.0, 'unit': 'serving'}
            }
        }
    ]
    """

    return create_objs(Ingredient, data)

def get_steps(data):
    """
    get the steps/ instructions for a given food using its id

    EXAMPLE DATA
    [
        {
            'number': 1,
            'step': 'Put enough olive oil in the bottom of a pie pan to lightly coat the bottom of the pan.'
        },
        {
            'number': 2,
            'step': 'Sprinkle with sea salt.'
        }
    ]
    """
    return create_objs(Step, data)
