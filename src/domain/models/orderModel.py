from dataclasses import dataclass

@dataclass
class ItemOrderModel:
    name: str
    price_per_unit: float
    total: float

@dataclass
class BeerRoundModel:
    name: str
    quantity: int 

@dataclass
class RoundModel:
    created: str
    items: BeerRoundModel

@dataclass
class OrderModel:
    created: str
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    items: ItemOrderModel
    rounds: RoundModel