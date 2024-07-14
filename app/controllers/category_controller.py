from flask import jsonify, request
from app.models.category import Category
from app.connectors.sql_connector import Session
from app.utils.api_response import api_response

def get_categories():
    session = Session()
    session.begin()

    try:
        product_categories = session.query(Category).all()
        return [category.serialize() for category in product_categories]
    except Exception as e:
        session.rollback()
        return jsonify(f"error occured: {e}"), 400
    finally:
        session.close()

def get_category_detail(category_id):
    session = Session()
    session.begin()

    try:
        category_products = session.query(Category).filter((Category.id==category_id)).first()
        if category_products:
            return api_response(
                status_code = 200,
                message =  "fetch category id success",
                data = {
                    'id': category_products.id,
                    'name': category_products.name
                }
            )
        else:
            return jsonify({"message":"category product you're looking for not found"})
    except Exception as e:
        session.rollback()
        return jsonify(f"fetching category detail failed:{e}"), 400
    finally:
        session.close()