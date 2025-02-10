from ..stock.factory import StockInteractorFactory
from ....domain.models.orderModel import ItemOrderModel
from functools import reduce

class CalculateTotalOrderUsecases(object):

    def __init__(self, order_repo):
        self.order = order_repo.get()
        stock_usecase = StockInteractorFactory()
        self.stock = stock_usecase.get().execute()

    def productSearchAndUpdate(self, item):
        productFound = None
        beersUpdate = []

        for beer in self.stock.beers:
            if beer.name.upper() == item.name.upper() and beer.quantity >= item.quantity:
                beer.quantity -= item.quantity
                productFound = beer
            beersUpdate.append(beer)

        self.stock.beers = beersUpdate
        return productFound

    def setItemFromRounds(self):
        try:
            for beerRound in self.order.rounds:
                for item in beerRound.items:
                    product = self.productSearchAndUpdate(item) 
                    if product:
                        self.order.items.append(
                            ItemOrderModel(
                                name=item.name,
                                price_per_unit=product.price,
                                total= product.price * item.quantity
                            )
                        )
        except Exception as error:
            print('-- setItemFromRounds', error)
            
    def setSubtotal(self):
        self.order.subtotal = sum(item.total for item in self.order.items)
            
    def setDiscounts(self):
        pass
            
    def setTaxes(self):
        self.order.taxes = 0.16
            
    def execute(self):
        self.setItemFromRounds()
        self.setSubtotal()
        self.setDiscounts()
        self.setTaxes()

        return self.order