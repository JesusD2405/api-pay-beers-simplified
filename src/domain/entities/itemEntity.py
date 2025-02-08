
class Item(object):
    def __init__(self, name, price_per_unit, total):
        self._name= name
        self._price_per_unit= price_per_unit
        self._total= total
        
    @property
    def name(self):
        return self._name
        
    @property
    def price_per_unit(self):
        return self._price_per_unit
        
    @property
    def total(self):
        return self._total