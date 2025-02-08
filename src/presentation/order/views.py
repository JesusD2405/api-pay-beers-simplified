from ...domain.usecases.order.factory import OrderInteractorFactory


class OrderView(object):

    @staticmethod
    def get():
        return OrderInteractorFactory.get()