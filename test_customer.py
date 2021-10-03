import unittest
from classes import Basket, Catalogue, Customer, External, PaymentDetails, Product, StoreFront

class CustomerTests(unittest.TestCase):
    def test_basket_attribute_is_Basket_instance_expect_true(self):
        #Act
        cust1 = Customer()
        #Assert
        self.assertTrue(isinstance(cust1.basket, Basket))

    def test_set_basket_attribute_to_string_expect_TypeError(self):
        #Arrange
        cust1 = Customer()
        test_basket = 'basket'
        #Act
        try:
            cust1.basket = test_basket
        #Assert
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
            self.assertEqual('The basket must be an instance of the Basket class', str(e))
        else:
            self.fail('TypeError not raised')

    def test_set_basket_attribute_to_Basket_expect_no_error(self):
        #Arrange
        cust1 = Customer()
        test_basket = Basket()
        #Act
        try:
            cust1.basket = test_basket
        #Assert
        except:
            self.fail('Setting basket attribute raised an error unexpectedly')
        self.assertEqual(cust1.basket, test_basket)

    def test_payment_details_attribute_is_Payment_Details_instance_expect_true(self):
        #Act
        cust1 = Customer()
        #Assert
        self.assertTrue(isinstance(cust1.payment_details, PaymentDetails))

    def test_set_payment_details_attribute_to_string_expect_TypeError(self):
        #Arrange
        cust1 = Customer()
        test_payment_details = 'payment details'
        #Act
        try:
            cust1.payment_details = test_payment_details
        #Assert
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
            self.assertEqual('The payment_details must be an instance of the PaymentDetails class', str(e))
        else:
            self.fail('TypeError not raised')

    def test_set_payment_details_attribute_to_payment_details_expect_no_error(self):
        #Arrange
        cust1 = Customer()
        test_payment_details = PaymentDetails()
        #Act
        try:
            cust1.payment_details = test_payment_details
        #Assert
        except:
            self.fail('Setting payment_details attribute raised an error unexpectedly')
        self.assertEqual(cust1.payment_details, test_payment_details)

class ExternalSellerTests(unittest.TestCase):
    def test_catalogue_attribute_is_Catalogue_instance_expect_true(self):
        #Act
        seller1 = External()
        #Assert
        self.assertTrue(isinstance(seller1.catalogue, Catalogue))

    def test_set_catalogue_attribute_to_string_expect_TypeError(self):
        #Arrange
        seller1 = External()
        test_catalogue = 'catalogue'
        #Act
        try:
            seller1.catalogue = test_catalogue
        #Assert
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
            self.assertEqual('The catalogue must be an instance of the Catalogue class', str(e))
        else:
            self.fail('TypeError not raised')

    def test_set_catalogue_attribute_to_Catalogue_expect_no_error(self):
        #Arrange
        seller1 = External()
        test_catalogue = Catalogue()
        #Act
        try:
            seller1.catalogue = test_catalogue
        #Assert
        except:
            self.fail('Setting catalogue attribute raised an error unexpectedly')
        self.assertEqual(seller1.catalogue, test_catalogue)

    def test_delivery_type_attribute_default_expect_FIRST_CLASS(self):
        #Act
        seller1 = External()
        #Assert
        self.assertEqual(seller1.delivery_type, 'FIRST CLASS')

    def test_set_delivery_type_attribute_not_in_DELIVERY_TYPES_expect_ValueError(self):
        #Arrange
        seller1 = External()
        #Act
        try:
            seller1.delivery_type = 'WALKING'
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Not a valid delivery type', str(e))
        else:
            self.fail('ValueError not raised')

    def test_storefront_attribute_is_StoreFront_instance_expect_true(self):
        #Act
        seller1 = External()
        #Assert
        self.assertTrue(isinstance(seller1.storefront, StoreFront))

    def test_set_storefront_attribute_to_string_expect_TypeError(self):
        #Arrange
        seller1 = External()
        test_storefront = 'storefront'
        #Act
        try:
            seller1.storefront = test_storefront
        #Assert
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
            self.assertEqual('The storefront must be an instance of the StoreFront class', str(e))
        else:
            self.fail('TypeError not raised')

    def test_set_storefront_attribute_to_StoreFront_expect_no_error(self):
        #Arrange
        seller1 = External()
        test_storefront = StoreFront()
        #Act
        try:
            seller1.storefront = test_storefront
        #Assert
        except:
            self.fail('Setting storefront attribute raised an error unexpectedly')
        self.assertEqual(seller1.storefront, test_storefront)

class BasketTests(unittest.TestCase):
    def test_products_attribute_is_a_list(self):
        #Act
        basket1 = Basket()
        #Assert
        self.assertTrue(isinstance(basket1.products, list))

    def test_set_products_attribute_to_string_expect_TypeError(self):
        #Arrange
        basket1 = Basket()
        test_products = 'products'
        #Act
        try:
            basket1.products = test_products
        #Assert
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
            self.assertEqual('The products attribute must be a list of Products', str(e))
        else:
            self.fail('TypeError not raised')

    def test_set_products_attribute_to_list_of_Products_expect_no_error(self):
        #Arrange
        basket1 = Basket()
        product1 = Product()
        product2 = Product()
        test_products = [product1, product2]
        #Act
        try:
            basket1.products = test_products
        #Assert
        except:
            self.fail('Setting storefront attribute raised an error unexpectedly')
        self.assertEqual(basket1.products, test_products)

    def test_set_products_attribute_to_list_of_strings_expect_TypeError(self):
        #Arrange
        basket1 = Basket()
        test_product1 = 'product1'
        test_product2 = 'product2'
        test_products = [test_product1, test_product2]
        #Act
        try:
            basket1.products = test_products
        #Assert
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
            self.assertEqual('The products attribute must be a list of Products', str(e))
        else:
            self.fail('TypeError not raised')

    def test_add_product_to_empty_basket_expect_basket_to_contain_one_product(self):
        #Arrange
        basket1 = Basket()
        test_product1 = Product()
        #Act
        basket1.add_product(test_product1)
        #Assert
        self.assertEqual(len(basket1.products), 1)
        self.assertEqual(basket1.products[0], test_product1)

    def test_add_string_to_empty_basket_expect_TypeError(self):
        #Arrange
        basket1 = Basket()
        test_product1 = 'product1'
        #Act
        try:
            basket1.add_product(test_product1)
        #Assert
        except TypeError as e:
            self.assertEqual(type(e), TypeError)
            self.assertEqual('You can only add objects of the type Product', str(e))
        else:
            self.fail('TypeError not raised')
        self.assertEqual(len(basket1.products), 0)

    def test_add_product_to_basket_expect_basket_to_contain_one_extra_product(self):
        #Arrange
        basket1 = Basket()
        test_product1 = Product()
        test_product2 = Product()
        basket1.products = [test_product1]
        num_products_pre_test = len(basket1.products)
        #Act
        basket1.add_product(test_product2)
        #Assert
        self.assertEqual(len(basket1.products), num_products_pre_test + 1)
        self.assertTrue(test_product2 in basket1.products)

    def test_remove_product_expect_basket_to_contain_one_less_product(self):
        #Arrange
        basket1 = Basket()
        test_product1 = Product()
        test_product2 = Product()
        basket1.products = [test_product1, test_product2]
        num_products_pre_test = len(basket1.products)
        #Act
        basket1.remove_product(test_product2)
        #Assert
        self.assertEqual(len(basket1.products), num_products_pre_test - 1)
        self.assertTrue(test_product2  not in basket1.products)

    def test_remove_product_not_in_basket_expect_ValueError(self):
        #Arrange
        basket1 = Basket()
        test_product1 = Product()
        test_product2 = Product()
        basket1.products = [test_product1]
        #Act
        try:
            basket1.remove_product(test_product2)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('The basket does not contain this product', str(e))
        else:
            self.fail('ValueError not raised')

    def test_remove_product_from_empty_basket_expect_ValueError(self):
        #Arrange
        basket1 = Basket()
        test_product1 = Product()
        #Act
        try:
            basket1.remove_product(test_product1)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('The basket does not contain this product', str(e))
        else:
            self.fail('ValueError not raised')

    def test_empty_basket_expect_basket_to_contain_no_products(self):
        #Arrange
        basket1 = Basket()
        test_product1 = Product()
        test_product2 = Product()
        basket1.products = [test_product1, test_product2]
        #Act
        basket1.empty_basket()
        #Assert
        self.assertEqual(len(basket1.products), 0)

if __name__ == '__main__':
  unittest.main()