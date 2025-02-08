
class StockRepository(object):
    
    def __init__(self, get_stock_usecase):
        self._get_stock_usecase = get_stock_usecase
    
    def get(self):
        try:
            body = self._get_stock_usecase.execute()
            status = 200

        except Exception as error:
            body = { 'error': str(error) }
            status = 500
        
        return body, status