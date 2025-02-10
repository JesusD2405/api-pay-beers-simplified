from .orderMockSerializer import OrderMockSerializer
import json
import os

class OrderMockRepository(object):

    def __init__(self):
        self.file_path = os.getcwd()+"/src/data/mockRepository/order/orderData.json"

    def get(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)

            return OrderMockSerializer.mapFrom(data)

        except Exception as error:
            return { 'error': str(error) }
        