from ....data.mockRepository.stock.stockMockRepository import StockMockRepository
from ...repository.stockRepository import StockRepository
from .getStockUsecases import GetStockUsecases

class StockRepoFactory(object):

    @staticmethod
    def get():
        return StockMockRepository()


class StockInteractorFactory(object):

    @staticmethod
    def get():
        repo_factory = StockRepoFactory.get()
        stock_usecases = GetStockUsecases(repo_factory)
        stock_repo = StockRepository(stock_usecases)
        return stock_repo