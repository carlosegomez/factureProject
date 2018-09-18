import unittest
# import sys
# sys.path.append('../')

from facture import (Client, Product, ProductLine, Facture)


class FactureComponentsTestCase(unittest.TestCase):

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
        self.assertEqual(product_line.price, product_1.price * product_line.quantity)


class FactureTestCase(unittest.TestCase):

    def setUp(self):
        self.client_1 = Client.Client("Pepe", "Mojica", "34567", "44 avenida de la part, Uruguay")
        product_1 = Product.Product("Avion", "flight game", 45.0)
        product_2 = Product.Product("100 anos de soledad", "book", 10.0)
        self.product_lines = [
            ProductLine.ProductLine(product_1, 3),
            ProductLine.ProductLine(product_2, 12)
        ]
        self.facture = Facture.Facture(.1, self.client_1, self.product_lines)

    def test_tva_value(self):
        self.assertEqual(self.facture.tva, .1)

    def test_product_lines_content(self):
        self.assertEqual(self.facture.product_lines, self.product_lines)

    def test_client_content(self):
        self.assertEqual(self.facture.client, self.client_1)

    def test_net_price_calcule(self):
        self.assertEqual(self.facture.net_price, 255.0)

    def test_tva_calcule(self):
        self.assertEqual(self.facture.only_tva, 25.5)

    def test_total_price_calcule(self):
        self.assertEqual(self.facture.total_price, 280.5)


if __name__ == '__main__':
    unittest.main()
