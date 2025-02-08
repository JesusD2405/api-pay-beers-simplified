from .orderMockData import OrderMockData
from .orderMockSerializer import OrderMockSerializer

class OrderMockRepository(object):

    def get(self):
        try:
            orderData = OrderMockData()
            order = orderData.get()

            return OrderMockSerializer.mapFrom(order)

        except Exception as error:
            return { 'error': str(error) }
        