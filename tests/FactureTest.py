import unittest
import factory
import random
import sys
sys.path.append('../')
from facture import (Client, Product, ProductLine, Facture)
from faker import Faker
from faker.providers import BaseProvider


fake = Faker()


class ProductNameProvider(BaseProvider):

    product_names = {'avion', 'board', 'tchupi book', 'screen'}

    def product_name(self):
        return self.random_element(self.product_names)


class ProductPriceProvider(BaseProvider):

    def product_price(self):
        return round(random.uniform(10, 100), 2)


fake.add_provider(ProductNameProvider)
fake.add_provider(ProductPriceProvider)


class ClientFactory(factory.Factory):
    class Meta:
        model = Client.Client
    name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    phone = factory.Faker('phone_number')
    address = factory.Faker('address')


class ProductFactory(factory.Factory):
    class Meta:
        model = Product.Product
    name = factory.lazy_attribute(lambda n: fake.product_name())
    desc = ""
    price = factory.lazy_attribute(lambda p: fake.product_price())


class ProductLineFactory(factory.Factory):
    class Meta:
        model = ProductLine.ProductLine
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker('random_int', min=1, max=10)


class FactureFactory(factory.Factory):
    class Meta:
        model = Facture.Facture
    tva = 0.1
    client = factory.SubFactory(ClientFactory)
    product_lines = factory.List(factory.SubFactory(ProductLineFactory) for i in range(random.randint(1, 10)))


class FactureComponentsTestCase(unittest.TestCase):

    def test_client(self):
        client_fake = ClientFactory()
        client_1 = Client.Client(client_fake.name, client_fake.last_name, client_fake.phone, client_fake.address)
        self.assertEqual(client_1.name, client_fake.name)
        self.assertEqual(client_1.last_name, client_fake.last_name)
        self.assertEqual(client_1.phone, client_fake.phone)
        self.assertEqual(client_1.address, client_fake.address)

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
        self.tva = 0.1
        self.client = ClientFactory()
        self.product_lines = [
            ProductLineFactory() for i in range(random.randint(1, 10))
        ]
        self.facture = Facture.Facture(self.tva, self.client, self.product_lines)

    def test_tva_value(self):
        self.assertEqual(self.facture.tva, .1)

    def test_product_lines_content(self):

        self.assertEqual(self.facture.product_lines, self.product_lines)

    def test_client_content(self):
        self.assertEqual(self.facture.client, self.client)

    def test_net_price_calcule(self):
        net_price = sum(line.price for line in self.product_lines)
        self.assertEqual(round(self.facture.net_price, 2), round(net_price, 2))

    def test_tva_calcule(self):
        net_price = sum(line.price for line in self.product_lines)
        self.assertEqual(round(self.facture.only_tva, 2), round(net_price * self.tva, 2))

    def test_total_price_calcule(self):
        net_price = sum(line.price for line in self.product_lines)
        total = net_price * (1 + self.tva)
        self.assertEqual(round(self.facture.total_price, 2), round(total, 2))


def content_generator():
    from jinja2 import Environment, FileSystemLoader
    env = Environment(
        loader=FileSystemLoader('../templates')
    )
    template = env.get_template('facture.html')
    facture = FactureFactory()
    return template.render(facture=facture)


def generate_pdf(content, filename):
    from weasyprint import HTML
    from weasyprint.fonts import FontConfiguration
    font_config = FontConfiguration()
    html = HTML(string=content)
    html.write_pdf(filename, font_config=font_config)


def generate_html(content, filename):
    import pathlib
    pathlib.Path('/tmp/report.html').write_text(content)


if __name__ == '__main__':
    unittest.main()
    content = content_generator()
    generate_pdf(content, '/tmp/report.pdf')
    generate_html(content, '/tmp/report.html')
