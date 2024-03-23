"""
Handles the add to cart funtionality
"""
from flask import Blueprint, request, jsonify
from app.models import Cart
from app.models import Product
from app.models import combine_pc

cart_api = Blueprint('cart_api', __name__)

@cart_api.route('/delete_cart/<int:product_id>', methods=['GET'], strict_slashes=False)
def deleteone_cart(product_id):
    """
    delete_cart : function to remove product from users cart
    agrguments:
        product_id: removes products by its id
    return: success on pass and error on failure
    """
    from app import Session
    try:
        session = Session()
        product_in_cart = session.query(Cart).filter(Cart.products.any(id=product_id)).first()
        if product_in_cart:
            product = session.query(Product).get(product_id)
            product_in_cart.products.remove(product)
            session.commit()
            return jsonify({'success': 'cart item deleted successfully'})
        else:
            return jsonify({'error': 'Product not found in the cart'})
    except Exception as e:
        return jsonify({"error": str(e)})


@cart_api.route('/get-cart/<int:user_id>', methods=['GET'], strict_slashes=False)
def get_cart(user_id):
    from app import Session
    product_dict = {}
    try: 
        session = Session()
        product = session.query(Cart).filter_by(user_id=user_id).first()

        combo = session.query(combine_pc).filter_by(cart_id=product.id).all()
        results = [tuple(row) for row in combo]
        session.close()
        return jsonify(results)
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}) 


@cart_api.route('/add_to_cart', methods=['POST'], strict_slashes=False)
def add_to_cart():
    """
    add_to_cart: endpoint implements the cart func
    accepsts: json datatype
    """
    from app import Session
    try:
        data = request.get_json()
        product_id = data.get('product_id')
        user_id = data.get('user_id')
        print(user_id)

        if not product_id:
            return jsonify({'error': 'Product ID is required'}), 400

        session = Session()
        products = session.query(Product).get(product_id)

        if not products:
            session.close()
            return jsonify({'error': 'Product not found'}), 404

        cart = session.query(Cart).filter_by(user_id=user_id).first()

        if not cart:
            cart = Cart(quantity=1, user_id=user_id)
            session.add(cart)

        cart.products.append(products)
        print(products.id)

        session.commit()
        session.close()

        return jsonify({'message': product_id})

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


