
from ....domain.models.orderModel import ItemOrderModel
import json

class ItemMockSerializer(object):
    
    @staticmethod
    def mapFrom(item):
        return ItemOrderModel(
            name= item['name'],
            price_per_unit= item['price_per_unit'],
            total= item['total'],
        )

    
    @staticmethod
    def mapTo(item):
        return json.dumps({
            "name": item.beer,
            "price_per_unit": item.beer,
            "total": item.beer
        })
