from flask import jsonify, request
from app.models.women import Women
from app.connectors.sql_connector import Session
from app.utils.api_response import api_response

def create_women_product():
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
    
    women_new_product = Women(
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
        session.add(women_new_product)
        session.commit()

    except Exception as e:
        session.rollback()
        return jsonify(f"add new product for women section failed: {e}"), 400
    
    return api_response(
        status_code = 201,
        message = "Add new product in women section success!!!",
        data = {
            "id": women_new_product.id,
            "category": women_new_product.category,
            "product_name": women_new_product.product_name,
            "product_brand": women_new_product.product_brand,
            "image_url": women_new_product.image_url,
            "rent_price": women_new_product.rent_price,
            "retail_price": women_new_product.retail_price,
            "size": women_new_product.size
        }
    )

def get_women_product():
    response_data = dict()
    session = Session()
    session.begin()

    try:
        women_product_query = session.query(Women)

        if request.args.get('query') != None:
            search_women_product_query = request.args.get('query')
            women_product_query = women_product_query.filter(Women.category.like(f"%{search_women_product_query}%"))

        women_products = women_product_query.all()
        response_data['women_products'] = [women.serialize(full=False) for women in women_products]
        return jsonify(response_data)
    except Exception as e:
        session.rollback()
        return jsonify(f"get women products failed: {e}"), 400
    finally:
        session.close()

def get_women_product_detail(women_product_id):
    session = Session()
    session.begin()
    
    try:
        women_product = session.query(Women).filter((Women.id==women_product_id)).first()
        if women_product:
            return jsonify(women_product.serialize(full=True))
        else:
            return jsonify({"message: women's product you're looking for not found"})
    except Exception as e:
        session.rollback()
        return jsonify(f"fetching women's product detail failed: {e}"), 400
    finally:
        session.close()

def delete_women_product(women_product_id):
    session = Session()
    session.begin()

    try:
        women_product_to_delete = session.query(Women).filter(Women.id==women_product_id).first()

        if women_product_to_delete is None:
            return jsonify({"message" : "women's product you're looking for not found"}), 404
        
        session.delete(women_product_to_delete)
        session.commit()

        return jsonify({"message" : "women's product delete successfully"})
    
    except Exception as e:
        session.rollback()
        return jsonify(f"delete women product failed: {e}"), 400
    
    finally:
        session.close()
    