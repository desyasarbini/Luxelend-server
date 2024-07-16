from flask import jsonify
from app.models.property import Property
from app.connectors.sql_connector import Session

def get_property():
    try:
        response_data = {}
        session = Session()

        propertiy = session.query(Property).all()
        response_data['propertiy'] = [prop.serialize() for prop in propertiy]

        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()