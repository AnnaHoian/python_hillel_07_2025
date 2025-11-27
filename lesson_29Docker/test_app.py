"""
test_app.py

CRUD function tests:
- test_add_product
- test_get_products
- test_update_product
- test_delete_product
"""

from app import add_product, get_products, update_product, delete_product

def test_add_product():
    product = add_product("Test Banana", 5.55, "sweet")
    assert product.id is not None

def test_get_products():
    products = get_products()
    assert isinstance(products, list)

def test_update_product():
    product = add_product("Test Peach", 3.00)
    updated = update_product(product.id, 7.00)
    assert float(updated.price) == 7.00

def test_delete_product():
    product = add_product("Test Pear", 4.44)
    delete_product(product.id)
    after = get_products()
    ids = [p.id for p in after]
    assert product.id not in ids

if __name__ == "__main__":
    test_add_product()
    test_get_products()
    test_update_product()
    test_delete_product()
