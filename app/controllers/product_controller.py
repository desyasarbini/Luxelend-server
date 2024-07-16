from flask import jsonify, request
from sqlalchemy.orm import joinedload
from app.models.product import Product
from app.models.product_properties import Product_properties
from app.models.property import Property
from app.models.property_category import Property_category
from app.connectors.sql_connector import Session
from app.utils.api_response import api_response

def get_product():
    response_data = dict()
    session = Session()
    session.begin()

    try:
        product_query = session.query(Product).options(
            joinedload(Product.product_properties)
            .joinedload(Product_properties.property)
            .joinedload(Property.property_category)
        )

        if request.args.get('query') is not None:
            search_query = request.args.get('query')
            product_query = product_query.filter(Product.name.like(f"%{search_query}%"))

        products = product_query.all()
        response_data['products'] = [product.serialize(full=True) for product in products]

        return jsonify(response_data)
    except Exception as e:
        session.rollback()
        return jsonify(f"Error occurred: {e}"), 400
    finally:
        session.close()

def get_product_detail(product_id):
    session = Session()
    session.begin()

    try:
        product_detail = session.query(Product).options(
            joinedload(Product.category), 
            joinedload(Product.gender_category),
            joinedload(Product.product_image),
            joinedload(Product.product_properties).joinedload(Product_properties.property).joinedload(Property.property_category)
        ).filter(Product.id == product_id).first()
        
        if product_detail:
            return api_response(
                status_code=200,
                message="Fetching product detail success!",
                data=product_detail.serialize(full=True)
            )
        else:
            return api_response(
                status_code=404,
                message="Product not found!",
                data={}
            )
        
    except Exception as e:
        session.rollback()
        return jsonify(f"Fetching product detail failed: {e}"), 400
    finally:
        session.close()
