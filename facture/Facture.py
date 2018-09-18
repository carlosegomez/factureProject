from dataclasses import dataclass
from facture import (ProductLine, Client)


@dataclass
class Facture:
    tva: float
    client: Client
    product_lines: ProductLine

    @property
    def net_price(self):
        return sum(product_line.price for product_line in self.product_lines)

    @property
    def only_tva(self):
        return self.net_price * self.tva

    @property
    def total_price(self):
        return self.net_price + self.only_tva
