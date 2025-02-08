
class OrderRepository(object):
    
    def __init__(self, get_order_usecase):
        self._get_order_usecase = get_order_usecase
    
    def get(self):
        try:
            body = self._get_order_usecase.execute()
            status = 200

        except Exception as error:
            body = { 'error': str(error) }
            status = 500
        
        return body, status