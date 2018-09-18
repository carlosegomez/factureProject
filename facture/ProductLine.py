from dataclasses import dataclass
import facture.Product as Product


@dataclass
class ProductLine:
    product: Product
    quantity: int = 0

    @property
    def price(self):
        return self.product.price * self.quantity
