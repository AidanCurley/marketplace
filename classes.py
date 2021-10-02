import re
from datetime import date

CARD_REGEX = re.compile(r'[\d]{16}')
CVV_REGEX = re.compile(r'[\d]{3}')
EMAIL_REGEX = re.compile(r'[\w]*@[\w]*\.[\w]*')
USER_TYPES = ['PERSON', 'ORGANISATION']
PAYMENT_TYPES = ['CARD', 'ONLINE']
CARD_TYPES = ['VISA', 'MASTERCARD']

class Customer:
    def __init__(self):
        self._basket = Basket()
        self._payment_details = None

    @property
    def basket(self):
        return self._basket

    @basket.setter
    def basket(self, new_basket):
        self._name = new_basket

    @property
    def payment_details(self):
        return self._payment_details

    @payment_details.setter
    def payment_details(self, new_payment_details):
        self._name = new_payment_details

class User(Customer):
    def __init__(self):
        self._name = None
        self._address = None
        self._username = None
        self._password = None
        self._email = None
        self._phone = None
        self._type = None

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

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, new_type):
        if new_type.upper() not in USER_TYPES:
            raise ValueError('Not a valid user type')
        else:
            self._type = new_type

class Basket:
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, new_products):
        self._products = new_products

    def add_product(self, new_product):
        self._products.append(new_product)

    def remove_product(self, product):
        self._products.remove(product)

    def empty_basket(self):
        self._products = []

    def checkout(self):
        return Transaction(date.today(), self)

class Transaction:
    def __init__(self, date_in, basket_in):
        self._date = date_in
        self._basket = basket_in
        self._promotional_code = None
        self._payment_method = None

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
        self._basket = new_basket

    @property
    def promotional_code(self):
        return self._promotional_code

    @promotional_code.setter
    def promotional_code(self, new_promotional_code):
        self._promotional_code = new_promotional_code

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, new_payment_method):
        self._payment_method = new_payment_method

    def calculate_total(self):
        pass

    def is_promotional_code_valid(self):
        return True

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
    def __init__(self):
        self._card_number = None
        self._card_type = None
        self._expiry_date = None
        self._cvv_number = None

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, new_card_number):
        if re.fullmatch(CARD_REGEX, new_card_number) == None:
            raise ValueError('Card number must be 16 digits long')
        else:
            self._card_number = new_card_number

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, new_card_type):
        if new_card_type.upper() not in CARD_TYPES:
            raise ValueError('Card type is invalid')
        else:
            self._card_type = new_card_type

    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, new_expiry_date):
        if new_expiry_date < date.today():
            raise ValueError('This card is expired')
        else:
            self._expiry_date = new_expiry_date

    @property
    def cvv_number(self):
        return self._cvv_number

    @cvv_number.setter
    def cvv_number(self, new_cvv_number):
        if re.fullmatch(CVV_REGEX, new_cvv_number) == None:
            raise ValueError('The CVV number must contain three digits')
        else:
            self._cvv_number = new_cvv_number

#  Small test just to check properties of user
user = User()
user.username = 'red1809'
user.password = '123456'
print(user.password)
user.email = 'red@hotmail.com'
print(user.email)
user.type = 'PERSON'
print(user.type)

# Checking fields on card class
card = Card()
card.card_number='1234567890123456'
print(card.cvv_number)
print(card.expiry_date)