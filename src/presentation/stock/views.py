from ...domain.usecases.stock.factory import StockInteractorFactory


class StockView(object):

    @staticmethod
    def get():
        return StockInteractorFactory.get()