from flask import Blueprint
from app.controllers.men_product_controller import create_men_product

men_product_blueprint = Blueprint('create_men_product',__name__)

men_product_blueprint.route("/men/product/create", methods = ["POSTS"])(create_men_product)