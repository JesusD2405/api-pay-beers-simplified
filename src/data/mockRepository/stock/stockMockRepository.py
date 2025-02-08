from ....domain.entities.stockEntity import Stock
from .stockMockData import StockMockData
from .stockMockSerializer import StockMockSerializer

class StockMockRepository(object):

    def get(self):
        try:
            stockData = StockMockData()
            stock = stockData.get()

            return StockMockSerializer.mapFrom(stock)

        except Exception as error:
            return { 'error': str(error) }
        