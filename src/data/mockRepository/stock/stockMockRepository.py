from .stockMockSerializer import StockMockSerializer
import json
import os
class StockMockRepository(object):
    def __init__(self):
        self.file_path = os.getcwd()+"/src/data/mockRepository/stock/stockData.json"

    def get(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)

            return StockMockSerializer.mapFrom(data)

        except Exception as error:
            return { 'error': str(error) }
        