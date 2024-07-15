from flask import Blueprint
from app.controllers.product_properties_controller import get_product_properties 

product_properties_bp_blueprint = Blueprint('product_properties_bp', __name__)

product_properties_bp_blueprint.route("/product_properties_bp", methods=["GET"])(get_product_properties)


