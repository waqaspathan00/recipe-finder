""" this file manages our different views """
from flask import Blueprint, render_template
from website.controllers.recipe_controller import RecipeController

views = Blueprint("views", __name__)

@views.route("/")
def index():
    """ the default path is to index.html """
    return render_template("index.html")

@views.route("/", methods=["POST"])
def get_foods_by_name():
    """ display the food results for a user searched food """
    return RecipeController.post_name()

@views.route("/recipe", methods=["GET"])
def recipe():
    """ display the ingredients and steps for a desired food """
    return RecipeController.get()

@views.route("/fridge", methods=["POST", "GET"])
def get_foods_by_ingredients():
    """ display the foods results for foods containing matching ingredients entered by user """
    return RecipeController.post_ingredients()
