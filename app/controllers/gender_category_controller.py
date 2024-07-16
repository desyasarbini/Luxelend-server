from flask import jsonify, request
from app.models.gender_category import Gender_category
from app.connectors.sql_connector import Session

def get_gender_category():
    response_data = dict()
    session = Session()
    session.begin()

    try:
        gender_category_query = session.query(Gender_category)
        
        if request.args.get('query') is not None:
            search_query = request.args.get('query')
            gender_category_query = gender_category_query.filter(Gender_category.gender_id.like(f"%{search_query}%"))

        gender_category = gender_category_query.all()
        response_data['gender_category'] = [gc.serialize() for gc in gender_category]

        return jsonify(response_data)
    except Exception as e:
        session.rollback()
        return jsonify({"error": f"Failed to fetch gender categories: {str(e)}"}), 400
    finally:
        session.close()

def get_gender_category_detail(gender_category_id):
    session = Session()
    session.begin()

    try:
        gender_categories = session.query(Gender_category).filter((Gender_category.id==gender_category_id)).first()
        
        if gender_categories:
            return jsonify(gender_categories.serialize(full=True))
        else:
            return jsonify({"message":"gender category not found"})
    except Exception as e:
        session.rollback()
        return jsonify(f"fetching gender category detail failed:{e}"), 400
    finally:
        session.close()

