import unittest
import sys
sys.path.append('../')

from facture import (Client, Product, ProductLine, Facture)


class FactureTestCase(unittest.TestCase):

    def test_client(self):
        client_1 = Client.Client("Pepe", "Mojica", "34567", "44 avenida de la part, Uruguay")
        self.assertEqual(client_1.name, "Pepe")
        self.assertEqual(client_1.last_name, "Mojica")
        self.assertEqual(client_1.phone, "34567")
        self.assertEqual(client_1.address, "44 avenida de la part, Uruguay")

    def test_product(self):
        product = Product.Product("Avion", "flight game", 45.0)
        self.assertEqual(product.name, "Avion")
        self.assertEqual(product.desc, "flight game")
        self.assertEqual(product.price, 45.0)

    def test_product_line(self):
        product_1 = Product.Product("Avion", "flight game", 45.0)
        product_line = ProductLine.ProductLine(product_1, 3)
        self.assertEqual(product_line.product, product_1)
        self.assertEqual(product_line.quantity, 3)

    def test_facture(self):
        client_1 = Client.Client("Pepe", "Mojica", "34567", "44 avenida de la part, Uruguay")
        product_1 = Product.Product("Avion", "flight game", 45.0)
        product_2 = Product.Product("100 anos de soledad", "book", 10.0)
        product_lines = [
            ProductLine.ProductLine(product_1, 3),
            ProductLine.ProductLine(product_2, 12)
        ]
        facture = Facture.Facture(.1, client_1, product_lines)
        self.assertEqual(facture.tva, .1)
        self.assertEqual(facture.product_lines, product_lines)
        self.assertEqual(facture.client, client_1)


if __name__ == '__main__':
    unittest.main()
