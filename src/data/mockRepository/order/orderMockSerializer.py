
class OrderMockSerializer(object):
    
    @staticmethod
    def mapFrom(order):
        return {
            'created': order['created'],
            'paid': order['paid'],
            'subtotal': order['subtotal'],
            'taxes': order['taxes'],
            'discounts': order['discounts'],
            'items': order['items'],
            'rounds': order['rounds'],
        }
    
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
