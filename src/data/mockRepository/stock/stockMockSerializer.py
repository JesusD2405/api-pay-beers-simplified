
from ....domain.models.stockModel import StockModel
from ..product.productMockSerializer import ProductMockSerializer
import json
class StockMockSerializer(object):
    
    @staticmethod
    def mapFrom(stock):
        return StockModel(
            last_updated= stock['last_updated'],
            beers= list(map(lambda beer: ProductMockSerializer.mapFrom(beer), stock['beers']))
        ) 

    
    @staticmethod
    def mapTo(stock):
        _beers = list(map(lambda beer: ProductMockSerializer.mapTo(beer), stock.beers))

        return json.dumps({
            "last_updated": stock.last_updated,
            "beers": _beers
        })
