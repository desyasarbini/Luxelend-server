from flask import Blueprint
from app.controllers.gender_category_controller import (
    get_gender_category, 
    get_gender_category_detail
)

gender_category_blueprint = Blueprint('gender_category', __name__)

gender_category_blueprint.route("/gender_category", methods=["GET"])(get_gender_category)

gender_category_blueprint.route("/gender_category/<gender_category_id>", methods=["GET"])(get_gender_category_detail)