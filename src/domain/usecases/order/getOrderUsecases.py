
from .calculateTotalOrderUsecases import CalculateTotalOrderUsecases
class GetOrderUsecases(object):

    def __init__(self, order_repo):
        self._order_repo = order_repo

    def execute(self):
        self._order_repo.get()
        total_order = CalculateTotalOrderUsecases(self._order_repo).execute()
        
        return total_order