from flask import jsonify, request
from sqlalchemy.orm import joinedload
from app.models.product import Product
from app.models.product_image import Product_image
from app.connectors.sql_connector import Session
from app.utils.api_response import api_response

def get_product():
    response_data = dict()
    session = Session()
    session.begin()

    try:
        product_query = session.query(Product)
        if request.args.get('query') != None:
            search_query = request.args.get('query')
            product_query = product_query.filter(Product.name.like(f"%{search_query}%"))

        products = product_query.all()
        response_data['products'] = [product.serialize(full=False) for product in products]

        return jsonify(response_data)
    except Exception as e:
        session.rollback()
        return jsonify(f"error occured: {e}"), 400
    finally:
        session.close()

def get_product_detail(product_id):
    session = Session()
    session.begin()

    try:
        product_detail = session.query(Product).options(
            joinedload(Product.category), 
            joinedload(Product.product_image),
            joinedload(Product.product_properties)
            ).filter((Product.id==product_id)).first()
        
        if product_detail:
            return api_response(
                status_code = 200,
                message = "fetching detail product success!",
                data = product_detail.serialize(full=True)
            )
        else:
            return api_response(
                status_code=404,
                message="Product not found!",
                data={}
            )
        
    except Exception as e:
        session.rollback()
        return jsonify(f"fetching product detail failed: {e}"), 400
    finally:
        session.close()

# def get_image_product(product_id):
#     session = Session()
#     session.begin()

#     try:
#         image_product = session.query(Product_image).filter(Product_image.product_id==product_id).first()
#         if image_product:
#             return jsonify(image_product.serialize)
#         else:
#             return jsonify({
#                 "message": "image not found"
#             })
        
#     except Exception as e:
#         session.rollback()
#         return jsonify(f"fetching product detail failed: {e}"), 400
