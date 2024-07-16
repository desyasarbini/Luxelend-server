from flask import Blueprint
from app.controllers.product_controller import (
    get_product, 
    get_product_detail, 
)

product_blueprint = Blueprint('product', __name__)

product_blueprint.route("/product", methods=["GET"])(get_product)

product_blueprint.route("/product/<product_id>", methods=["GET"])(get_product_detail)