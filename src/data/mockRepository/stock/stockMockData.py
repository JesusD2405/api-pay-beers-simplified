
class StockMockData():
    def __init__(self):
        self._stock = {
            "last_updated": "2024-09-10 12:00:00",
            "beers": [
                {
                    "name": "Corona",
                    "price": 115,
                    "quantity": 2
                },
                {
                    "name": "Quilmes",
                    "price": 120,
                    "quantity": 0
                },
                {
                    "name": "Club Colombia",
                    "price": 110,
                    "quantity": 3
                }
            ]
        }
    
    def get(self):
        return self._stock