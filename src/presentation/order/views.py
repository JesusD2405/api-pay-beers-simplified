from ...domain.usecases.order.factory import OrderInteractorFactory
from ...domain.repository.orderRepository import OrderRepository

class OrderView(object):

    @staticmethod
    def get():
        order_usecases = OrderInteractorFactory.get()

        return OrderRepository(order_usecases)