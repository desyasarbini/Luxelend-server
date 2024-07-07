from flask import Blueprint
from app.controllers.women_product_controller import (
    create_women_product, 
    get_women_product, 
    get_women_product_detail, 
    delete_women_product
)

women_product_blueprint = Blueprint('create_women_product',__name__)

women_product_blueprint.route("/women/product/create", methods=["POST"])(create_women_product)

women_product_blueprint.route("/women/product", methods=["GET"])(get_women_product)

women_product_blueprint.route("/women/product/<women_product_id>", methods=["GET"])(get_women_product_detail)

women_product_blueprint.route("/women/product/<women_product_id>", methods=["DELETE"])(delete_women_product)