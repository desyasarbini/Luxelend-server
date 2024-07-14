from flask import Blueprint
from app.controllers.gender_category_controller import get_gender

gender_category_blueprint = Blueprint('gender_category_endpoint', __name__)

gender_category_blueprint.route("/gender", methods=["GET"])(get_gender)