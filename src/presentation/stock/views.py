from ...domain.repository.stockRepository import StockRepository
from ...domain.usecases.stock.factory import StockInteractorFactory


class GetStockView(object):

    @staticmethod
    def get():
        get_stock_interactor = StockInteractorFactory.get()
        return StockRepository(get_stock_interactor)