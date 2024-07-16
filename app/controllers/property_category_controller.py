from flask import jsonify, request
from app.models.property_category import Property_category
from app.connectors.sql_connector import Session

def get_property_category():
    try:
        response_data = {}
        session = Session()

        property_category = session.query(Property_category).all()
        response_data['property_category'] = [prop.serialize() for prop in property_category]
        
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

