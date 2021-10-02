import re
from datetime import date

EMAIL_REGEX = re.compile(r'[\w]*@[\w]*\.[\w]*')
TYPES = ['PERSON', 'ORGANISATION']

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
        if new_type not in TYPES:
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









user = User()
user.username = 'red1809'
user.password = '123456'
print(user.password)
user.email = 'red@hotmail.com'
print(user.email)
user.type = 'PERSON'
print(user.type)