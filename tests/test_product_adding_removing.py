import pytest


def test_product_adding_removing(app):
    app.add_few_items_to_cart(3)
    app.delete_items_from_cart()
