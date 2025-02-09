
class Stock(object):
    def __init__(self, last_updated, beers):
        self._last_updated = last_updated
        self._beers = beers
    
    @property
    def last_updated(self):
        return self._last_updated

    @property
    def beers(self):
        return self._beers