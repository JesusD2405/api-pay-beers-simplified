from ...domain.usecases.stock.factory import StockInteractorFactory
from ...domain.repository.stockRepository import StockRepository

class StockView(object):

    @staticmethod
    def get():
        stock_usecases = StockInteractorFactory.get()

        return StockRepository(stock_usecases)