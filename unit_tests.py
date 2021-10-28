"""Contains unit tests for the classes and their methods"""
import unittest
from errors import *
from classes import Basket, Catalogue, Customer, External, PaymentDetails, OnlinePayment, Product, Card, Voucher
from datetime import date, datetime

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
            self.assertEqual('The storefront must be a png/jpeg file', str(e))
        else:
            self.fail('TypeError not raised')

    def test_set_storefront_attribute_to_png_expect_no_error(self):
        #Arrange
        seller1 = External()
        test_storefront = 'storefront.png'
        #Act
        try:
            seller1.storefront = test_storefront
        #Assert
        except:
            self.fail('Setting storefront attribute raised an error unexpectedly')
        self.assertEqual(seller1.storefront, test_storefront)


class BasketTests(unittest.TestCase):
    def create_test_product(self):
        return Product([1,2,3,4])

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
        product1 = self.create_test_product()
        product2 = self.create_test_product()
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
        test_product1 = self.create_test_product()
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
        test_product1 = self.create_test_product()
        test_product2 = self.create_test_product()
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
        test_product1 = self.create_test_product()
        test_product2 = self.create_test_product()
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
        test_product1 = self.create_test_product()
        test_product2 = self.create_test_product()
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
        test_product1 = self.create_test_product()
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
        test_product1 = self.create_test_product()
        test_product2 = self.create_test_product()
        basket1.products = [test_product1, test_product2]
        #Act
        basket1.empty_basket()
        #Assert
        self.assertEqual(len(basket1.products), 0)


class CardTests(unittest.TestCase):
    VALID_CARD_NUMBER = "1112223334445556"
    INVALID_CARD_NUMBER = "123451234512345a"
    SHORT_CARD_NUMBER = "1"
    LONG_CARD_NUMBER = "123123123123123123123"


    VALID_SORT_CODE = "123456"
    INVALID_SORT_CODE = "12345a"
    SHORT_SORT_CODE = "12345"
    LONG_SORT_CODE = "1234567"

    VALID_CARD_TYPE = "VISA"
    INVALID_CARD_TYPE = "INVALID"

    VALID_EXPIRY = "2025-01-31"
    EXPIRED_EXPIRY = "2020-01-01"
    INVALID_EXPIRY = "January 2023"

    VALID_CVV = "123"
    INVALID_CVV = "abc"
    SHORT_CVV = "12"
    LONG_CVV = "1234"

    def test_create_card_with_valid_parameters_expect_no_errors(self):
        #Arrange & Act
        card1 = Card(self.VALID_CARD_NUMBER, self.VALID_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.VALID_CVV)
        #Assert
        self.assertEqual(card1.card_number, self.VALID_CARD_NUMBER)
        self.assertEqual(card1.sort_code, self.VALID_SORT_CODE)
        self.assertEqual(card1.card_type, self.VALID_CARD_TYPE)
        self.assertEqual(card1.expiry_date, self.VALID_EXPIRY)
        self.assertEqual(card1.cvv_number, self.VALID_CVV)

    def test_create_card_with_no_card_number_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card('', self.VALID_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Card number must be 16 digits long', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_invalid_card_number_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.INVALID_CARD_NUMBER, self.VALID_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Card number must be 16 digits long', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_short_card_number_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.SHORT_CARD_NUMBER, self.VALID_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Card number must be 16 digits long', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_long_card_number_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.LONG_CARD_NUMBER, self.VALID_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Card number must be 16 digits long', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_no_sort_code_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, '', self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Sort code must contain 6 digits', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_invalid_sort_code_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.INVALID_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Sort code must contain 6 digits', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_short_sort_code_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.SHORT_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Sort code must contain 6 digits', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_long_sort_code_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.LONG_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Sort code must contain 6 digits', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_no_cvv_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.VALID_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, '')
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('CVV must contain 3 digits', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_invalid_cvv_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.VALID_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.INVALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('CVV must contain 3 digits', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_short_cvv_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.VALID_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.SHORT_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('CVV must contain 3 digits', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_long_cvv_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.VALID_SORT_CODE, self.VALID_CARD_TYPE, self.VALID_EXPIRY, self.LONG_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('CVV must contain 3 digits', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_no_expiry_date_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.VALID_SORT_CODE, self.VALID_CARD_TYPE, '', self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Invalid date format', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_invalid_expiry_date_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.VALID_SORT_CODE, self.VALID_CARD_TYPE, self.INVALID_EXPIRY, self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Invalid date format', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_expired_expiry_date_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.VALID_SORT_CODE, self.VALID_CARD_TYPE, self.EXPIRED_EXPIRY, self.VALID_CVV)
        #Assert
        except ExpiryError as e:
            self.assertEqual(type(e), ExpiryError)
            self.assertEqual('This card is expired', str(e))
        else:
            self.fail('ExpiryError not raised')

    def test_create_card_with_no_card_type_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.VALID_SORT_CODE, '', self.VALID_EXPIRY, self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Invalid card type', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_card_with_invalid_card_type_expect_ValueError(self):
        #Arrange & Act
        try:
          card1 = Card(self.VALID_CARD_NUMBER, self.VALID_SORT_CODE, self.INVALID_CARD_TYPE, self.VALID_EXPIRY, self.VALID_CVV)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Invalid card type', str(e))
        else:
            self.fail('ValueError not raised')


class OnlinePaymentTests(unittest.TestCase):
    VALID_SERVICE_NUMBER = "1234"
    INVALID_SERVICE_NUMBER = "abcd"
    SHORT_SERVICE_NUMBER = "123"
    LONG_SERVICE_NUMBER = "12345"

    VALID_SERVICE_NAME = "Paypal"
    INVALID_SERVICE_NAME = 12345

    VALID_BALANCE = 1000.0
    INVALID_BALANCE = "£1000"
    NEGATIVE_BALANCE = -100.0

    def test_create_online_payment_with_valid_parameters_expect_no_errors(self):
        #Arrange & Act
        online_payment1 = OnlinePayment(self.VALID_SERVICE_NAME, self.VALID_SERVICE_NUMBER, self.VALID_BALANCE)
        #Assert
        self.assertEqual(online_payment1.service_name, self.VALID_SERVICE_NAME)
        self.assertEqual(online_payment1.service_number, self.VALID_SERVICE_NUMBER)
        self.assertEqual(online_payment1.balance, self.VALID_BALANCE)


    def test_create_online_payment_with_no_service_name_expect_ValueError(self):
        #Arrange & Act
        try:
          online_payment1 = OnlinePayment('', self.VALID_SERVICE_NUMBER, self.VALID_BALANCE)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Invalid service name', str(e))
        else:
            self.fail('ValueError not raised')

    def test_online_payment_with_invalid_service_name_expect_ValueError(self):
        #Arrange & Act
        try:
          online_payment1 = OnlinePayment(self.INVALID_SERVICE_NAME, self.VALID_SERVICE_NUMBER, self.VALID_BALANCE)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Invalid service name', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_online_payment_with_no_service_number_expect_ValueError(self):
        #Arrange & Act
        try:
          online_payment1 = OnlinePayment(self.VALID_SERVICE_NAME, '', self.VALID_BALANCE)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Online service number must be 4 digits long', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_online_payment_with_invalid_service_number_expect_ValueError(self):
        #Arrange & Act
        try:
          online_payment1 = OnlinePayment(self.VALID_SERVICE_NAME, self.INVALID_SERVICE_NUMBER, self.VALID_BALANCE)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Online service number must be 4 digits long', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_online_payment_with_short_service_number_expect_ValueError(self):
        #Arrange & Act
        try:
          online_payment1 = OnlinePayment(self.VALID_SERVICE_NAME, self.SHORT_SERVICE_NUMBER, self.VALID_BALANCE)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Online service number must be 4 digits long', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_online_payment_with_long_service_number_expect_ValueError(self):
        #Arrange & Act
        try:
          online_payment1 = OnlinePayment(self.VALID_SERVICE_NAME, self.LONG_SERVICE_NUMBER, self.VALID_BALANCE)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Online service number must be 4 digits long', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_online_payment_with_no_balance_expect_balance_to_default_to_0_point_0(self):
        #Arrange & Act
        online_payment1 = OnlinePayment(self.VALID_SERVICE_NAME, self.VALID_SERVICE_NUMBER)
        #Assert
        self.assertEqual(online_payment1.balance, 0.0)

    def test_create_online_payment_with_invalid_balance_expect_ValueError(self):
        #Arrange & Act
        try:
          online_payment1 = OnlinePayment(self.VALID_SERVICE_NAME, self.VALID_SERVICE_NUMBER, self.INVALID_BALANCE)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Invalid balance', str(e))
        else:
            self.fail('ValueError not raised')

    def test_create_online_payment_with_negative_balance_expect_ValueError(self):
        #Arrange & Act
        try:
          online_payment1 = OnlinePayment(self.VALID_SERVICE_NAME, self.VALID_SERVICE_NUMBER, self.NEGATIVE_BALANCE)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Balance cannot be less than zero', str(e))
        else:
            self.fail('ValueError not raised')

    def test_process_payment_expect_correct_new_balance(self):
        #Arrange
        online_payment1 = OnlinePayment(self.VALID_SERVICE_NAME, self.VALID_SERVICE_NUMBER, self.VALID_BALANCE)
        #Act
        online_payment1.process_payment(100)
        #Assert
        self.assertEqual(online_payment1.balance, 900.0)

    def test_process_payment_with_amount_greater_than_balance_expect_ValueError(self):
        #Arrange
        online_payment1 = OnlinePayment(self.VALID_SERVICE_NAME, self.VALID_SERVICE_NUMBER, self.VALID_BALANCE)
        #Act
        try:
            online_payment1.process_payment(90000)
        #Assert
        except PaymentError as e:
            self.assertEqual(type(e), PaymentError)
            self.assertEqual('Not enough credit in your account', str(e))
        else:
            self.fail('PaymentError not raised')


class VoucherTests(unittest.TestCase):
    VALID_EXPIRY = "2025-01-31"
    EXPIRED_EXPIRY = "2020-01-01"
    INVALID_EXPIRY = "January 2023"

    def test_voucher_with_valid_parameters_expect_no_errors(self):
        #Arrange & Act
        voucher1 = Voucher('1111', self.VALID_EXPIRY, 100)
        #Assert
        self.assertEqual(voucher1.voucher_id, '1111')
        self.assertEqual(voucher1.expiry_date, self.VALID_EXPIRY)
        self.assertEqual(voucher1.balance, 100)

    def test_voucher_with_invalid_expiry_date_expect_ValueError(self):
        #Arrange & Act
        try:
            voucher1 = Voucher('1111', self.INVALID_EXPIRY, 100)
        #Assert
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            self.assertEqual('Invalid date format', str(e))
        else:
            self.fail('ValueError not raised')

    def test_voucher_with_expired_expiry_date_expect_ExpiryError(self):
        #Arrange & Act
        try:
            voucher1 = Voucher('1111', self.EXPIRED_EXPIRY, 100)
        #Assert
        except ExpiryError as e:
            self.assertEqual(type(e), ExpiryError)
            self.assertEqual('This voucher is expired', str(e))
        else:
            self.fail('ExpiryError not raised')

    def test_process_payment_with_amount_less_than_balance_expect_no_PaymentError(self):
        #Arrange
        voucher1 = Voucher('1111', self.VALID_EXPIRY, 100)
        #Act
        try:
            voucher1.process_payment(99)
        #Assert
        except PaymentError as e:
            self.fail('PaymentError raised')


    def test_process_payment_with_amount_greater_than_balance_expect_PaymentError(self):
        #Arrange
        voucher1 = Voucher('1111', self.VALID_EXPIRY, 100)
        #Act
        try:
            voucher1.process_payment(90000)
        #Assert
        except PaymentError as e:
            self.assertEqual(type(e), PaymentError)
            self.assertEqual('The voucher cannot cover the cost of this transaction', str(e))
        else:
            self.fail('PaymentError not raised')


if __name__ == '__main__':
  unittest.main()