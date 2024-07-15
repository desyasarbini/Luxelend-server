from flask import Blueprint
from app.controllers.property_controler import get_property

property_blueprint = Blueprint('property', __name__)

property_blueprint.route("/property", methods=["GET"])(get_property)
