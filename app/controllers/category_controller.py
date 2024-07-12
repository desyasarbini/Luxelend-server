from flask import jsonify, request
from app.models.category import Category
from app.connectors.sql_connector import Session
from app.utils.api_response import api_response

def get_categories():
    session = Session()
    session.begin()

    try:
        product_categoories = session.query(Category).all()
        return [category.serialize() for category in product_categoories]
    except Exception as e:
        session.rollback()
        return jsonify(f"error occured: {e}"), 400
    finally:
        session.close()