from flask import jsonify, request
from app.models.men import Men
from app.connectors.sql_connector import Session
from app.utils.api_response import api_response

def create_men_product():
    session = Session()
    session.begin()

    category = request.json.get("category")
    product_name = request.json.get("product_name")
    product_brand = request.json.get("product_brand")
    image_url = request.json.get("image_url")
    rent_price = request.json.get("rent_price")
    retail_price = request.json.get("retail_price")
    size = request.json.get("size")
    color = request.json.get("color")
    style = request.json.get("style")
    material = request.json.get("material")
    fit_note = request.json.get("fit_note")
    
    men_new_product = Men(
        category = category,
        product_name = product_name,
        product_brand = product_brand,
        image_url = image_url,
        rent_price = rent_price,
        retail_price = retail_price,
        size = size,
        color = color,
        style = style,
        material = material,
        fit_note = fit_note
    )
    
    try:
        session.add(men_new_product)
        session.commit()

    except Exception as e:
        session.rollback()
        return jsonify(f"add new product for men section failed: {e}"), 400
    
    return api_response(
        status_code = 201,
        message = "Add new product in men section success!!!",
        data = {
            "id": men_new_product.id,
            "category": men_new_product.category,
            "product_name": men_new_product.product_name,
            "product_brand": men_new_product.product_brand,
            "image_url": men_new_product.image_url,
            "rent_price": men_new_product.rent_price,
            "retail_price": men_new_product.retail_price,
            "size": men_new_product.size
        }
    )

def get_men_product():
    response_data = dict()
    session = Session()
    session.begin()
    try:
        men_product_query = session.query(Men)

        if request.args.get('query') != None:
            search_men_product_query = request.args.get('query')
            men_product_query = men_product_query.filter(Men.category.like(f"%{search_men_product_query}%"))

        men_products = men_product_query.all()
        response_data['men_products'] = [men.serialize(full=False) for men in men_products]
        return jsonify(response_data)
    
    except Exception as e:
        session.rollback()
        return jsonify(f"get men products failed: {e}"), 400
    finally:
        session.close()

def get_men_product_detail(men_product_id):
    session = Session()
    session.begin()

    try:
        men_product = session.query(Men).filter((Men.id==men_product_id)).first()
        if men_product:
            return jsonify(men_product.serialize(full=True))
        else:
            return jsonify({"message: men's product you're looking for not found"})
    except Exception as e:
        session.rollback()
        return jsonify(f"fetching men's product detail failed: {e}"), 400
    finally:
        session.close()

def get_men_product_category():
    session = Session()
    session.begin()

def delete_men_product(men_product_id):
    session = Session()
    session.begin()

    try:
        men_product_to_delete = session.query(Men).filter(Men.id==men_product_id).first()

        if men_product_to_delete is None:
            return jsonify({"message" : "men's product you're looking for not found"}), 404
        
        session.delete(men_product_to_delete)
        session.commit()

        return jsonify({"message" : "men's product delete successfully"})
    
    except Exception as e:
        session.rollback()
        return jsonify(f"delete men product failed: {e}"), 400
    
    finally:
        session.close()
    