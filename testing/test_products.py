import unittest

from testing.products import Product, POSSystem


class TestPOS(unittest.TestCase):

    def test_get_all_products(self):
        product1 = Product(1, "thing", 15)
        product2 = Product(2, "thing2", 20)
        product3 = Product(3, "thing3", 25)

        pos = POSSystem()

        pos.products = {1: product1, 2: product2, 3: product3}

        result = pos.get_all_products()

        self.assertDictEqual(result, {1: product1, 2: product2, 3: product3})

        self.assertIsNone()

        self.assertListEqual()