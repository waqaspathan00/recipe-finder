""" this file manages our different views """
from flask import Blueprint, render_template
from website.controllers.recipe_controller import RecipeController

views = Blueprint("views", __name__)

@views.route("/")
def home():
    """ the default path is to home.html """
    return render_template("home.html")

@views.route("/", methods=["POST"])
def send_recipe():
    """ POST request logic lies within RecipeController """
    return RecipeController.post()
