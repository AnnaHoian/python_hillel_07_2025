"""
app.py

Contains the Product ORM model and CRUD functions for working with the products table.

Functionality:
- add_product(): creates a new product in the database
- get_products(): gets all products
- update_product(): updates the product price
- delete_product(): deletes the product
"""

from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey
from db import Base, get_session

class Product(Base):
    """ORM model representing products table"""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

class Category(Base):
    """ORM model representing category table"""
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

def add_product(name, price, description=None, category_id=None):
    """Adds a new product and returns it."""
    session = get_session()
    product = Product(
        name=name,
        price=price,
        description=description,
        category_id=category_id
    )
    session.add(product)
    session.commit()
    session.refresh(product)
    session.close()
    return product

def get_products():
    """Returns a list of all products."""
    session = get_session()
    products = session.query(Product).all()
    session.close()
    return products

def update_product(product_id, new_price):
    """Updates the price of a product by ID."""
    session = get_session()
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        product.price = new_price
        session.commit()
        session.refresh(product)
    session.close()
    return product

def delete_product(product_id):
    """Deletes product by ID."""
    session = get_session()
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        session.delete(product)
        session.commit()
    session.close()
