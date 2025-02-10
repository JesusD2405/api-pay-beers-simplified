from ....data.mockRepository.order.orderMockRepository import OrderMockRepository
from .getOrderUsecases import GetOrderUsecases

class OrderRepoFactory(object):

    @staticmethod
    def get():
        return OrderMockRepository()


class OrderInteractorFactory(object):

    @staticmethod
    def get():
        repo_factory = OrderRepoFactory.get()
        order_usecases = GetOrderUsecases(repo_factory)

        return order_usecases