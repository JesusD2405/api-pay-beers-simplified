
import json
from ....domain.models.productModel import ProductModel

class ProductMockSerializer(object):
    
    @staticmethod
    def mapFrom(product):
        return ProductModel(
            name= product['name'],
            price= product['price'],
            quantity= product['quantity']
        )

    
    @staticmethod
    def mapTo(product):
        return {
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity
        }
