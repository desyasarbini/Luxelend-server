from flask import Blueprint
from app.controllers.category_controller import get_categories

category_blueprint = Blueprint('category_endpoint', __name__)

category_blueprint.route("/category", methods=["GET"])(get_categories)