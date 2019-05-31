import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
    
    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)


class AcmeReportTests(unittest.TestCase):
    '''Test that report!'''
    def test_default_num_products(self):
        '''Test product list default length being 30'''
        products = generate_products()
        self.assertEqual(len(products),30)

    def test_legal_names(self):
        '''Make sure generated names are in the list'''   
        products = generate_products()
        adj = set()
        nouns = set()
        for product in products:
            adj.add(product.name.split()[0])
            nouns.add(product.name.split()[1])
        adj = list(adj)
        nouns = list(nouns)

        self.assertIn(adj,ADJECTIVES)
        self.assertIn(nouns,NOUNS)



if __name__ == '__main__':
    unittest.main()