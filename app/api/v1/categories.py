"""
Handles product categories
"""
from flask import Blueprint, jsonify
from app.models import Product

categories = Blueprint('categories', __name__)

@categories.route('/categories', methods=['GET'])
def get_category_all():
    """
    get_categor_all: endpoint to retrieve all categories in the database
    return: json datatype
    """
    from app import Session
    try:
        session = Session()
        category_list = []
        categories = session.query(Product.category).distinct().all()
        for category in categories:
            category_dict = {
                    'category': category[0]
                    }
            category_list.append(category_dict)
        session.close()
        return jsonify(category_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
