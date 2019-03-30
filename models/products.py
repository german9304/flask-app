
from .abtractproduct import AbstractProduct


class Products(AbstractProduct):

    def __init__(self, id, product, outOfStock, quantity, likes):
        """Init products class"""
        self.id = id
        self._product = product
        self.outOfStock = outOfStock
        self.quantity = quantity
        self.likes = likes

    def get_product(self):
        """Return product."""
        return self._product
