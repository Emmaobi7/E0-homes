import requests
from .models import Product

def fetch_and_store_products():
    """
    popluate database with initial dummy data
    """
    from . import Session
    session = Session()
    url = 'https://fakestoreapi.com/products'
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()

        for item in data:
            title = item.get('title')
            price = item.get('price')
            description = item.get('description')
            category = item.get('category')
            image = item.get('image')

            new_product = Product(title=title, price=price, description=description, category=category, image=image)
            session.add(new_product)

        session.commit()
        session.close()
        print("Data fetched and stored successfully.")
    else:
        print("Failed to fetch data from the API.")


