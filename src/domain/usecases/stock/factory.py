from ....data.mockRepository.stock.stockMockRepository import StockMockRepository
from .getStockUsecases import GetStockUsecases

class StockRepoFactory(object):

    @staticmethod
    def get():
        return StockMockRepository()


class StockInteractorFactory(object):

    @staticmethod
    def get():
        product_repo = StockRepoFactory.get()
        return GetStockUsecases(product_repo)