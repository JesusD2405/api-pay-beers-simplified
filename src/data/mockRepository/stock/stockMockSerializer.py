
class StockMockSerializer(object):
    
    @staticmethod
    def mapFrom(stock):
        return {
            'last_updated': stock['last_updated'],
            'beers': stock['beers']
        }
    
    @staticmethod
    def mapTo(stock):
        return {
            'last_updated': stock.last_updated,
            'beers': stock.beers
        }
