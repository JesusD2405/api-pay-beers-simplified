
from ....domain.models.stockModel import StockModel
from ..product.productMockSerializer import ProductMockSerializer
class StockMockSerializer(object):
    
    @staticmethod
    def mapFrom(stock):
        _beers = list(map(lambda beer: ProductMockSerializer.mapFrom(beer), stock['beers']))

        return StockModel(
            last_updated= stock['last_updated'],
            beers= _beers
        ) 

    
    @staticmethod
    def mapTo(stock):
        _beers = list(map(lambda beer: ProductMockSerializer.mapTo(beer), stock.beers))

        return {
            "last_updated": stock.last_updated,
            "beers": _beers
        }
