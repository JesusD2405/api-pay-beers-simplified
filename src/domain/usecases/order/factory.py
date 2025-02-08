from ....data.mockRepository.order.orderMockRepository import OrderMockRepository
from ...repository.orderRepository import OrderRepository
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
        order_repo = OrderRepository(order_usecases)
        return order_repo