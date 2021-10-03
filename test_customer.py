import unittest
from classes import Basket, Catalogue, Customer, External, PaymentDetails, StoreFront

class CustomerTests(unittest.TestCase):
    def test_basket_attribute_is_Basket_instance_expect_true(self):
        cust1 = Customer()
        self.assertTrue(isinstance(cust1.basket, Basket))

    def test_payment_details_attribute_is_Payment_Details_instance_expect_true(self):
        cust1 = Customer()
        self.assertTrue(isinstance(cust1.payment_details, PaymentDetails))

class ExternalSellerTests(unittest.TestCase):
    def test_catalogue_attribute_is_Catalogue_instance_expect_true(self):
        seller1 = External()
        self.assertTrue(isinstance(seller1.catalogue, Catalogue))

    def test_delivery_type_attribute_default_expect_FIRST_CLASS(self):
        seller1 = External()
        self.assertEqual(seller1.delivery_type, 'FIRST CLASS')

    def test_delivery_type_attribute_not_in_DELIVERY_TYPES_expect_ValueError(self):
        seller1 = External()
        try:
            seller1.delivery_type = "WALKING"
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Not a valid delivery type', str(e))
        else:
            self.fail('ValueError not raised')

    def test_storefront_attribute_is_StoreFront_instance_expect_true(self):
        seller1 = External()
        self.assertTrue(isinstance(seller1.storefront, StoreFront))

if __name__ == '__main__':
  unittest.main()