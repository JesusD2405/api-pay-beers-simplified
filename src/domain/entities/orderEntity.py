
class Order(object):
    def __init__(self, created, paid, subtotal, taxes, discounts, items, rounds):
        self._created = created
        self._paid = paid
        self._subtotal = subtotal
        self._taxes = taxes
        self._discounts = discounts
        self._items = items
        self._rounds = rounds
        
    @property
    def created(self):
        return self._created
        
    @property
    def paid(self):
        return self._paid
        
    @property
    def subtotal(self):
        return self._subtotal
        
    @property
    def taxes(self):
        return self._taxes
        
    @property
    def discounts(self):
        return self._discounts
        
    @property
    def items(self):
        return self._items
        
    @property
    def rounds(self):
        return self._rounds