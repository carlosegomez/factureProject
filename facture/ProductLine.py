from dataclasses import dataclass
import facture.Product as Product

@dataclass
class ProductLine:
    product: Product
    quantity: int = 0
