from ....domain.models.orderModel import OrderModel
from ..item.itemMockSerializer import ItemMockSerializer
from ..rounds.roundMockSerializer import RoundMockSerializer
class OrderMockSerializer(object):
    
    @staticmethod
    def mapFrom(order):
        return OrderModel(
            created= order['created'],
            paid= order['paid'],
            subtotal= order['subtotal'],
            taxes= order['taxes'],
            discounts= order['discounts'],
            items= list(map(lambda item: ItemMockSerializer.mapFrom(item), order['items'])),
            rounds= list(map(lambda beerRound: RoundMockSerializer.mapFrom(beerRound), order['rounds']))
        )
    
    @staticmethod
    def mapTo(order):
        return {
            'created': order.created,
            'paid': order.paid,
            'subtotal': order.subtotal,
            'taxes': order.taxes,
            'discounts': order.discounts,
            'items': order.items,
            'rounds': order.rounds
        }
