
class GetOrderUsecases(object):

    def __init__(self, order_repo):
        self._order_repo = order_repo

    def execute(self):
        return self._order_repo.get()