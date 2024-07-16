from flask import jsonify, request
from sqlalchemy.orm import joinedload
from app.connectors.sql_connector import Session
from app.models.product_properties import Product_properties
from app.models.product_image import Product_image

def get_product_properties():
    try:
        response_data = {}
        session = Session()

        product_properties_query = session.query(Product_properties)
        product_properties = product_properties_query.all()
        response_data['product_properties'] = [prop.serialize() for prop in product_properties]

        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": f"get product properties failed: {str(e)}"}), 400
    finally:
        session.close()



