"""
Handles user authentication
sign_up, login and logout
"""
from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/sign_up', methods=['POST'])
def sign_up():
    """
    sign_up: endpoint for user registration
    """
    from app import Session
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Invalid JSON data'}), 400

    email = data.get('email')
    first_name = data.get('first_name')
    password1 = data.get('password1')
    password2 = data.get('password2')

    if not email or not first_name or not password1 or not password2:
        return jsonify({'error': 'Missing required fields'}), 400

    if password1 != password2:
        return jsonify({'error': 'Passwords don\'t match'}), 400

    session = Session()

    existing_user = session.query(User).filter_by(email=email).first()

    if existing_user:
        session.close()
        return jsonify({'error': 'Email already exists'}), 409

    new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
    session.add(new_user)
    session.commit()
    login_user(new_user, remember=True)
    session.close()

    return jsonify({'message': 'User successfully registered', 'data': new_user.id}), 201


@auth_api.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """
    login: endpoint for user login
    """
    from app import Session
    data = request.get_json()
    print(data)

    if not data:
        return jsonify({'error': 'Invalid JSON data'}), 400

    email = data.get('email')
    password = data.get('password')
  

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    session = Session()

    user = session.query(User).filter_by(email=email).first()


    if user and check_password_hash(user.password, password):
        login_user(user, remember=True)
        session.close()
        return jsonify({'message': 'Login successful', 'data': user.id}), 200

    session.close()
    return jsonify({'error': 'Invalid email or password'}), 401

@auth_api.route('/logout', methods=['POST'])
def logout():
    """
    logout: logout user
    """
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

