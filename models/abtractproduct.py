
from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    def get_product(self):
        raise Exception('Class not implemented')
