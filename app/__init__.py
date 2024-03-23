"""
app blueprint
"""
from dotenv import load_dotenv
import os

load_dotenv()
db_password = os.getenv("DB_PASSWORD")

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from flask_login import LoginManager
from .models import User
from .v_api import fetch_and_store_products
from app.api.v1.products import products
from flask_cors import CORS
from app.api.v1.categories import categories
from app.api.v1.auth import auth_api
# from app.api.vi.payment import payment
from app.api.v1.cart import cart_api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'averysecuresomething'

# database connection
#engine = create_engine('mysql+mysqlconnector://foodie_dev:foodie_pwd@localhost:3306/foodie_db', pool_size=30, max_overflow=15, pool_pre_ping=True)

engine = create_engine('mysql+mysqlconnector://sql10693595:' + db_password + '@sql10.freemysqlhosting.net:3306/sql10693595', pool_size=30, max_overflow=15, pool_pre_ping=True)


Session = sessionmaker(bind=engine)
# app blueprints
app.register_blueprint(auth_api, url_prefix="/auth")
app.register_blueprint(products, url_prefix="/api/v1")
# app.register_blueprint(payment, url_prefix="/api/v1")

CORS(app, supports_credentials=True)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST", "PUT", "DELETE"], "headers": ["Content-Type", "Authorization"]}})
CORS(app)
app.register_blueprint(categories, url_prefix="/api/v1")
app.register_blueprint(cart_api, url_prefix="/api/v1")

# login manager
login_manager = LoginManager()
login_manager.login_view = 'auth_api.login'
login_manager.init_app(app)

session = Session()
@login_manager.user_loader
def load_user(id):
    return session.query(User).get(int(id))

@app.teardown_appcontext
def close_db(error):
    session.close()

# create database tables
Base.metadata.create_all(bind=engine)


"""
uncomment to populate database with fake store api
"""
#fetch_and_store_products()
