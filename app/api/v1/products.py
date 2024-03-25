"""
Handles getting products from the database
By id and seach functinality
"""
from flask import Blueprint, jsonify, request
from app.models import Product
import requests
import json
from dotenv import load_dotenv
import os



products = Blueprint('products', __name__)

@products.route('/verify_payment', methods=['POST'], strict_slashes=False)
def verify_payment():
    data = request.get_json()
    reference = data.get('reference')


    endpoint = 'https://api.paystack.co/transaction/verify/' + reference

    load_dotenv()
    paystack_sk = os.getenv("PAYSTACK_SECRET_KEY")
    headers = {
        'Authorization': 'Bearer ' + paystack_sk
    }
    try:

        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            
            return jsonify({'data': response.json()})
        else:
            
             return jsonify({'error': 'Internal server error'})
    except Exception as e:
        return jsonify({'error': str(e)})



@products.route('/payment', methods=['POST'], strict_slashes=False)
def initilize_payment():
    """
    initialize_payment: make payment 
    implemented using paystack transavtion api
    return: paystack api response
    """
    data = request.get_json()
    email = data.get('email')
    amount = data.get('amount')
    url = 'https://api.paystack.co/transaction/initialize'
    load_dotenv()
    paystack_sk = os.getenv("PAYSTACK_SECRET_KEY")
    headers = {
        'Authorization': 'Bearer ' + paystack_sk,
        'Content-Type': 'application/json'
    }
    payload = {
        'email': email,
        'amount': amount * 100
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return jsonify({'data': response.json()})
    except Exception as e:
        return jsonify(str(e))




@products.route('/products', methods=['GET'], strict_slashes=False)
def get_product_all():
    """
    get_product_all(): endpoint for retieving all
                        products in database
    """
    from app import Session
    try:
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=20, type=int)

        offset = (page - 1) * per_page
        session = Session()
        product_list = []
        product_obj = session.query(Product).offset(offset).limit(per_page).all()
        for product in product_obj:
            product_dict = {
                    'id': product.id,
                    'title': product.title,
                    'price': product.price,
                    'category': product.category,
                    'image': product.image,
                    'description': product.description
                    }
            product_list.append(product_dict)
        session.close()
        return jsonify(product_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@products.route('/products/<int:product_id>', methods=['GET'], strict_slashes=False)
def get_product_id(product_id):
    """
    get_product_id: endpoint to retrieve a product by id
    Args:
        product_id: an existing product id
    """
    from app import Session
    product_dict = {}
    try:
        session = Session()
        product = session.query(Product).filter_by(id=product_id).first()
        if product:
            product_dict = {
                    'id': product.id,
                    'title': product.title,
                    'price': product.price,
                    'category': product.category,
                    'image': product.image,
                    'description': product.description
                    }
        session.close()
        return jsonify(product_dict)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@products.route('/products/search/<string:query>', methods=['GET'])
def search_product(query):
    """
    search_product: endpoint for sorting database
    Args:
         query: by product title and category
    """
    from app import Session
    try:
        session = Session()
        search_list = []
        search_result = session.query(Product).filter((Product.title.ilike(f'%{query}%') | Product.category.ilike(f'%{query}%'))).all()
        for product in search_result:
            product_dict = {
                    'id': product.id,
                    'title': product.title,
                    'price': product.price,
                    'category': product.category,
                    'image': product.image,
                    'description': product.description
                    }
            search_list.append(product_dict)
        session.close()
        return jsonify(search_list)
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


