
from ....domain.models.productModel import ProductModel
import json

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
        return json.dumps({
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity
        })
