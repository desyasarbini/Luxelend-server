from flask import Blueprint
from app.controllers.category_controller import (
    get_categories, 
    get_category_detail
)

category_blueprint = Blueprint('category', __name__)

category_blueprint.route("/category", methods=["GET"])(get_categories)

category_blueprint.route("/category/<category_id>", methods=["GET"])(get_category_detail)