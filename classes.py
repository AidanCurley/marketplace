"""Contains hthe main classes used in the application"""
import re
from datetime import date, datetime
from errors import *
from constants import *


class Customer:
    def __init__(self):
        self._basket = Basket()
        self._payment_details = PaymentDetails()
        super().__init__()

    @property
    def basket(self):
        return self._basket

    @basket.setter
    def basket(self, new_basket):
        if isinstance(new_basket, Basket) == False:
            raise TypeError('The basket must be an instance of the Basket class')
        else:
            self._basket = new_basket

    @property
    def payment_details(self):
        return self._payment_details

    @payment_details.setter
    def payment_details(self, new_payment_details):
        if isinstance(new_payment_details, PaymentDetails) == False:
            raise TypeError('The payment_details must be an instance of the PaymentDetails class')
        else:
          self._payment_details = new_payment_details


class Catalogue:
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, new_products):
        self._products = new_products

    def add_product(self, new_product):
        if new_product in self.products:
            raise ValueError("Already exists in catalogue")
        else:
            self.products.append(new_product)

    def remove_product(self, unwanted_product):
        if unwanted_product not in self.products:
            raise ValueError("Product not found in catalogue")
        else:
            self.products.remove[unwanted_product]


class External:
    def __init__(self):
        self._catalogue = Catalogue()
        self._delivery_type = 'FIRST CLASS'
        self._storefront = None
        super().__init__()

    @property
    def catalogue(self):
        return self._catalogue

    @catalogue.setter
    def catalogue(self, new_catalogue):
        if isinstance(new_catalogue, Catalogue) == False:
            raise TypeError('The catalogue must be an instance of the Catalogue class')
        else:
            self._catalogue = new_catalogue

    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, new_delivery_type):
        if new_delivery_type not in DELIVERY_TYPES:
            raise ValueError('Not a valid delivery type')
        else:
            self._name = new_delivery_type

    @property
    def storefront(self):
        return self._storefront

    @storefront.setter
    def storefront(self, new_storefront):
        if re.fullmatch(STOREFRONT_REGEX, new_storefront) == None:
            raise TypeError('The storefront must be a png/jpeg file')
        else:
            self._storefront = new_storefront


class User(Customer, External):
    def __init__(self, idIn = None, usernameIn = None, passwordIn = None, nameIn = None):
        self._id = idIn
        self._username = usernameIn
        self._password = passwordIn
        self._name = nameIn
        self._address = None
        self._email = None
        self._phone = None
        self._type = None
        super().__init__()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        self._address = new_address

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        self._username = new_username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            raise ValueError('Password must be at least 6 characters long')
        else:
            self._password = new_password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if re.fullmatch(EMAIL_REGEX, new_email) == None:
                raise ValueError('Not a valid email address')
        else:
            self._email = new_email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, new_phone):
        self._phone = new_phone


class Product:
    def __init__(self, attributes):
        self.id = attributes[0]
        self._name = attributes[1]
        self._price = attributes[2]
        self._stock_count = attributes[3]

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @property
    def stock_count(self):
        return self._stock_count

    @stock_count.setter
    def stock_count(self, new_stock_count):
        self._stock_count = new_stock_count

    def is_available(self):
        return self.stock_count > 0

    def __str__(self):
        return f'{self.name}'


class Warehouse:
    def __init__(self):
        self._products = {}

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, new_products):
        self._products = new_products

    def add_product_to_warehouse(self, new_product, new_location):
        if new_product in self.products.keys():
            print("Already exists")
        else:
            self.products[new_product] = new_location

    def remove_product_from_warehouse(self, unwanted_product):
        if unwanted_product not in self.products.keys():
            print("Not in warehouse")
        else:
            del self.products[unwanted_product]
            print('Deleted')

    def update_location(self, product, new_location):
        self.products[product] = new_location

    def find_product(self, product):
        if product not in self.products.keys():
            print("Not in warehouse")
        else:
            return self.products[product]


class Basket:
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, new_products):
        if isinstance(new_products, list) == False:
            raise TypeError('The products attribute must be a list of Products')
        for product in new_products:
            if isinstance(product, Product) == False:
                raise TypeError('The products attribute must be a list of Products')
        self._products = new_products

    def add_product(self, new_product):
        if isinstance(new_product, Product) == False:
            raise TypeError('You can only add objects of the type Product')
        else:
            self._products.append(new_product)

    def remove_product(self, product):
        try:
            self._products.remove(product)
        except ValueError:
            raise ValueError('The basket does not contain this product')

    def empty_basket(self):
        self._products = []

    def calculate_total(self):
        return round(sum(product.price for product in self.products),2)

    def create_transaction(self, payment_method):
        return Transaction(date.today(), self, payment_method)

    def __str__(self):
        return f"Basket contains {[str(product) for product in self.products]}"


class Transaction:
    def __init__(self, dateIn, basketIn, payment_methodIn):
        self._date = dateIn
        self._basket = basketIn
        self._payment_details = payment_methodIn

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        self._date = new_date

    @property
    def basket(self):
        return self._basket

    @basket.setter
    def basket(self, new_basket):
        if isinstance(new_basket, Basket) == False:
            raise TypeError('Invalid basket in transaction')
        else:
            self._basket = new_basket

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, new_payment_method):
        if isinstance(new_payment_method, PaymentMethod) == False:
            raise TypeError('Invalid payment method in transaction')
        else:
            self._payment_method = new_payment_method


class Order:
    def __init__(self, new_transaction):
        self._transaction = new_transaction
        self._fulfilled = False
        self._fulfilled_by = None
        self._shipped = False


    @property
    def transaction(self):
        return self._transaction

    @transaction.setter
    def transaction(self, new_transaction):
        self._transaction = new_transaction

    @property
    def fulfilled(self):
        return self._fulfilled

    @fulfilled.setter
    def fulfilled(self, new_fulfilled):
        self._fulfilled = new_fulfilled

    @property
    def fulfilled_by(self):
        return self._fulfilled_by

    @fulfilled_by.setter
    def fulfilled_by(self, new_fulfilled_by):
        self._fulfilled_by = new_fulfilled_by

    @property
    def shipped(self):
        return self._shipped

    @shipped.setter
    def shipped(self, new_shipped):
        self._shipped = new_shipped

    def fulfill_order(self):
        pass

    def notify_customer(self):
        return True


class PaymentDetails:
    def __init__(self):
        self._card = None
        self._online_payment = None
        self._default = None

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, new_card):
        self._card = new_card

    @property
    def online_payment(self):
        return self._online_payment

    @online_payment.setter
    def online_payment(self, new_online_payment):
        self._online_payment = new_online_payment

    @property
    def default(self):
        return self._default

    @default.setter
    def default(self, new_default):
        if new_default.upper() not in PAYMENT_TYPES:
            raise ValueError('Not a valid payment type')
        else:
            self._default = new_default


class Card:
    def __init__(self, card_numberIn, sort_codeIn, card_typeIn, expiry_dateIn, cvv_numberIn):
        self.validate_card_details(card_numberIn, sort_codeIn, card_typeIn, expiry_dateIn, cvv_numberIn)
        self._card_number = card_numberIn
        self._sort_code = sort_codeIn
        self._card_type = card_typeIn
        self._expiry_date = expiry_dateIn
        self._cvv_number = cvv_numberIn
        super().__init__()

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, new_card_number):
        if self.is_valid_card_number(new_card_number):
            self._card_number = new_card_number

    def is_valid_card_number(self, card_number):
        if re.fullmatch(CARD_REGEX, card_number) == None:
            raise ValueError('Card number must be 16 digits long')
        else:
            return True

    @property
    def sort_code(self):
        return self._sort_code

    @sort_code.setter
    def sort_code(self, new_sort_code):
        if self.is_valid_sort_code(new_sort_code):
            self._sort_code = new_sort_code

    def is_valid_sort_code(self, sort_code):
        if re.fullmatch(SORT_CODE_REGEX, sort_code) == None:
            raise ValueError('Sort code must contain 6 digits')
        else:
            return True

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, new_card_type):
        if self.is_valid_card_type(new_card_type):
            self._card_type = new_card_type

    def is_valid_card_type(self, card_type):
        if card_type.upper() not in CARD_TYPES:
            raise ValueError('Invalid card type')
        else:
          return True

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, new_expiry_date):
        if self.is_valid_expiry_date(new_expiry_date):
            self._expiry_date = new_expiry_date

    def is_valid_expiry_date(self, dateIn):
        try:
            if datetime.strptime(str(dateIn), DATE_FORMAT) < datetime.now():
                raise ExpiryError('This card is expired')
        except ValueError:
            raise ValueError('Invalid date format')
        else:
            return True

    @property
    def cvv_number(self):
        return self._cvv_number

    @cvv_number.setter
    def cvv_number(self, new_cvv_number):
        if self.is_valid_cvv(new_cvv_number):
            self._cvv_number = new_cvv_number

    def is_valid_cvv(self, cvv):
        if re.fullmatch(CVV_REGEX, cvv) == None:
            raise ValueError('CVV must contain 3 digits')
        else:
            return True

    def validate_card_details(self, card_numberIn, sort_codeIn, card_typeIn, expiry_dateIn, cvv_numberIn):
        self.is_valid_card_number(card_numberIn)
        self.is_valid_sort_code(sort_codeIn)
        self.is_valid_card_type(card_typeIn)
        self.is_valid_expiry_date(expiry_dateIn)
        self.is_valid_cvv(cvv_numberIn)
        return

    def __str__(self):
        return f"{self.card_type} {self.card_number}"

class OnlinePayment:
    def __init__(self, service_nameIn, service_numberIn, balanceIn = 0.0):
        self.validate_service_details(service_nameIn, service_numberIn, balanceIn)
        self._service_name = service_nameIn
        self._service_number = service_numberIn
        self._balance = balanceIn
        super().__init__()

    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def name(self, new_service_name):
      if self.is_valid_service_name(new_service_name):
          self._service_name = new_service_name

    def is_valid_service_name(self, name):
        if type(name) != str or len(name) == 0:
            raise ValueError('Invalid service name')
        else:
            return True

    @property
    def service_number(self):
        return self._service_number

    @service_number.setter
    def service_number(self, new_service_number):
        if self.is_valid_service_number(new_service_number):
            self._service_number = new_service_number

    def is_valid_service_number(self, service_number):
        if re.fullmatch(ONLINE_SERVICE_NUMBER_REGEX, service_number) == None:
            raise ValueError('Online service number must be 4 digits long')
        else:
            return True

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if self.is_valid_balance(new_balance):
            self._balance = new_balance

    def is_valid_balance(self, balance):
        if type(balance) != float:
            raise ValueError('Invalid balance')
        elif balance < 0:
            raise ValueError('Balance cannot be less than zero')
        else:
            return True

    def validate_service_details(self, service_nameIn, service_numberIn, balanceIn):
        self.is_valid_service_name(service_nameIn)
        self.is_valid_service_number(service_numberIn)
        self.is_valid_balance(balanceIn)
        return

    def process_payment(self, debit_amount):
        if debit_amount > self.balance:
            raise PaymentError('Not enough credit in your account')
        else:
            self.balance -= debit_amount
            return self.balance

    def __str__(self):
        return f"{self.service_name} {self.service_number}"


class Voucher:
    def __init__(self, voucher_idIn, expiry_dateIn = "2022-01-01", balanceIn = 0):
        self._voucher_id = voucher_idIn
        if self.is_valid_expiry_date(expiry_dateIn):
            self._expiry_date = expiry_dateIn
        self._balance = balanceIn
        super().__init__()

    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, new_voucher_id):
        self._voucher_id = new_voucher_id

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, new_expiry_date):
        if self.is_valid_expiry_date(new_expiry_date):
            self._expiry_date = new_expiry_date

    def is_valid_expiry_date(self, dateIn):
        try:
            if datetime.strptime(str(dateIn), DATE_FORMAT) < datetime.now():
                raise ExpiryError('This voucher is expired')
        except ValueError:
            raise ValueError('Invalid date format')
        else:
            return True

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    def process_payment(self, payment):
        if self.balance < payment:
            raise PaymentError('The voucher cannot cover the cost of this transaction')
        else:
            return True

    def __str__(self):
        return f"Voucher number {self.voucher_id}"

class PaymentMethod(Card, OnlinePayment, Voucher):
    def __init__(self):
        super().__init__()

