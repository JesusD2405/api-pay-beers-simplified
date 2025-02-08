
class GetStockUsecases(object):

    def __init__(self, stock_repo):
        self._stock_repo = stock_repo

    def execute(self):
        return self._stock_repo.get()