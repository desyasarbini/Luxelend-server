from flask import jsonify, request
from app.connectors.sql_connector import Session  # Sesuaikan dengan modul koneksi Anda
from app.models.gender import Gender

def get_gender():
    try:
        session = Session()

        genders = session.query(Gender).all()
        serialized_genders = [gender.serialize() for gender in genders]

        return jsonify(serialized_genders), 200
    except Exception as e:
        return jsonify({"error": f"Failed to fetch genders: {str(e)}"}), 400
    finally:
        session.close()