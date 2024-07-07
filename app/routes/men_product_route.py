from flask import Blueprint
from app.controllers.men_product_controller import (
    create_men_product,
    get_men_product,
    get_men_product_detail,
    delete_men_product
)

men_product_blueprint = Blueprint('create_men_product',__name__)

men_product_blueprint.route("/men/product/create", methods=["POST"])(create_men_product)

men_product_blueprint.route("/men/product", methods=["GET"])(get_men_product)

men_product_blueprint.route("/men/product/<men_product_id>", methods=["GET"])(get_men_product_detail)

men_product_blueprint.route("/men/product/<men_product_id>", methods=["DELETE"])(delete_men_product)