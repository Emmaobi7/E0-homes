"""
Handles getting products from the database
By id and seach functinality
"""
from flask import Blueprint, jsonify, request
from app.models import Product

products = Blueprint('products', __name__)

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


