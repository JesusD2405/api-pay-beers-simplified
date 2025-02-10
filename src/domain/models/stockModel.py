
from dataclasses import dataclass
from .productModel import ProductModel

@dataclass
class StockModel:
    last_updated: str
    beers: ProductModel