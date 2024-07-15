from flask import Blueprint

from app.controllers.property_category_controller import get_property_category

property_category_blueprint = Blueprint('property_category', __name__)

property_category_blueprint.route("/property_category", methods=["GET"])(get_property_category)
