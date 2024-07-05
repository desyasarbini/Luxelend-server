from flask import jsonify, request
from app.models.men import Men
from app.connectors.sql_connector import Session
from app.utils.api_response import api_response

def create_men_product():
    session = Session()
    session.begin()
    
    men_new_product = Men(
        category = request.json.get("category", None),
        product_name = request.json.get("product_name", None),
        product_brand = request.json.get("product_brand", None),
        image_url = request.json.get("image_url", None),
        rent_price = request.json.get("rent_price", None),
        retail_price = request.json.get("retail_price", None),
        size = request.json.get("size", None),
        color = request.json.get("color", None),
        style = request.json.get("style", None),
        material = request.json.get("material", None),
        fit_note = request.json.get("fit_note", None)
    )
    
    try:
        session.add(men_new_product)
        session.commit()        
    except Exception as e:
        session.rollback()
        return jsonify(f"add new product for men section failed: {e}")
    finally:
        session.close()
        return api_response(
            status_code = 201,
            message = "Add new product in men section success!!!",
            data = {}
        )