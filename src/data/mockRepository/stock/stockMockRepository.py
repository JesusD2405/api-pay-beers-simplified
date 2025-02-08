from ....domain.entities.stockEntity import Stock
from .stockMockData import StockMockData

class StockMockRepository(object):

    def get(self):
        try:
            stockData = StockMockData()
            stock = stockData.get()
            return Stock(
                last_updated= stock['last_updated'],
                beers= stock['beers']
            )

        except Exception as error:
            return { 'error': str(error) }
        