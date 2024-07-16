from flask import jsonify
from app.connectors.sql_connector import Session  
from app.models.gender import Gender

def get_gender():
    try:
        session = Session()

        gender = session.query(Gender).all()
        serialized_genders = [gender.serialize() for gender in gender]
        return jsonify(serialized_genders), 200
    except Exception as e:
        return jsonify({"error": f"Failed to fetch genders: {str(e)}"}), 400
    finally:
        session.close()