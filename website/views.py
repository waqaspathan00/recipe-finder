""" this file manages our different views """
from flask import Blueprint, render_template
from website.controllers.recipe_controller import RecipeController

views = Blueprint("views", __name__)

@views.route("/")
def home():
    """ the default path is to home.html """
    return render_template("home.html")

@views.route("/", methods=["POST"])
def get_foods_by_name():
    """ display the food results for a user searched food """
    return RecipeController.post()

@views.route("/recipe", methods=["GET"])
def recipe():
    """ display the ingredients and steps for a desired food """
    return RecipeController.get()

