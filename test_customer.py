import unittest
from classes import Basket, Catalogue, Customer, External, PaymentDetails, StoreFront

class CustomerTests(unittest.TestCase):
    def test_basket_attribute_is_Basket_instance_expect_true(self):
        cust1 = Customer()
        self.assertTrue(isinstance(cust1.basket, Basket))

    def test_set_basket_attribute_to_string_expect_TypeError(self):
        cust1 = Customer()
        test_basket = 'basket'
        try:
            cust1.basket = test_basket
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
            self.assertEqual('The basket must be an instance of the Basket class', str(e))
        else:
            self.fail('TypeError not raised')

    def test_set_basket_attribute_to_Basket_expect_no_error(self):
        cust1 = Customer()
        test_basket = Basket()
        try:
            cust1.basket = test_basket
        except:
            self.fail('Setting basket attribute raised an error unexpectedly')
        self.assertEqual(cust1.basket, test_basket)

    def test_payment_details_attribute_is_Payment_Details_instance_expect_true(self):
        cust1 = Customer()
        self.assertTrue(isinstance(cust1.payment_details, PaymentDetails))

    def test_set_payment_details_attribute_to_string_expect_TypeError(self):
        cust1 = Customer()
        test_payment_details = 'payment details'
        try:
            cust1.payment_details = test_payment_details
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
            self.assertEqual('The payment_details must be an instance of the PaymentDetails class', str(e))
        else:
            self.fail('TypeError not raised')

    def test_set_payment_details_attribute_to_payment_details_expect_no_error(self):
        cust1 = Customer()
        test_payment_details = PaymentDetails()
        try:
            cust1.payment_details = test_payment_details
        except:
            self.fail('Setting payment_details attribute raised an error unexpectedly')
        self.assertEqual(cust1.payment_details, test_payment_details)

class ExternalSellerTests(unittest.TestCase):
    def test_catalogue_attribute_is_Catalogue_instance_expect_true(self):
        seller1 = External()
        self.assertTrue(isinstance(seller1.catalogue, Catalogue))

    def test_set_catalogue_attribute_to_string_expect_TypeError(self):
        seller1 = External()
        test_catalogue = 'catalogue'
        try:
            seller1.catalogue = test_catalogue
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
            self.assertEqual('The catalogue must be an instance of the Catalogue class', str(e))
        else:
            self.fail('TypeError not raised')

    def test_set_catalogue_attribute_to_Catalogue_expect_no_error(self):
        seller1 = External()
        test_catalogue = Catalogue()
        try:
            seller1.catalogue = test_catalogue
        except:
            self.fail('Setting catalogue attribute raised an error unexpectedly')
        self.assertEqual(seller1.catalogue, test_catalogue)

    def test_delivery_type_attribute_default_expect_FIRST_CLASS(self):
        seller1 = External()
        self.assertEqual(seller1.delivery_type, 'FIRST CLASS')

    def test_set_delivery_type_attribute_not_in_DELIVERY_TYPES_expect_ValueError(self):
        seller1 = External()
        try:
            seller1.delivery_type = 'WALKING'
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Not a valid delivery type', str(e))
        else:
            self.fail('ValueError not raised')

    def test_storefront_attribute_is_StoreFront_instance_expect_true(self):
        seller1 = External()
        self.assertTrue(isinstance(seller1.storefront, StoreFront))

    def test_set_storefront_attribute_to_string_expect_TypeError(self):
        seller1 = External()
        test_storefront = 'storefront'
        try:
            seller1.storefront = test_storefront
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
            self.assertEqual('The storefront must be an instance of the StoreFront class', str(e))
        else:
            self.fail('TypeError not raised')

    def test_set_storefront_attribute_to_StoreFront_expect_no_error(self):
        seller1 = External()
        test_storefront = StoreFront()
        try:
            seller1.storefront = test_storefront
        except:
            self.fail('Setting storefront attribute raised an error unexpectedly')
        self.assertEqual(seller1.storefront, test_storefront)

if __name__ == '__main__':
  unittest.main()