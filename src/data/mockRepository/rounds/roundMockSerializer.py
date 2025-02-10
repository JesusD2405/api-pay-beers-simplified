
import json
from ....domain.models.orderModel import RoundModel, BeerRoundModel

class RoundMockSerializer(object):
    
    @staticmethod
    def mapFrom(rounds):
        return RoundModel(
            created= rounds['created'],
            items= list(map(lambda item: BeerRoundModel(name= item['name'], quantity= item['quantity']), rounds['items']))
        )

    
    @staticmethod
    def mapTo(item):
        return json.dumps({
            "name": item.beer,
            "price_per_unit": item.beer,
            "total": item.beer
        })
