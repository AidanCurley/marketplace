import re
from datetime import date

EMAIL_REGEX = re.compile(r'[\w]*@[\w]*\.[\w]*')


class User:
    def __init__(self):
        self._username
        self._password
        self._email
        self._phone

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


class Person(User):
    def __init__(self, new_name, new_address):
        self._name = new_name
        self._address = new_address

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


class Organisation(User):
    def __init__(self, new_name, new_address):
        self._name = new_name
        self._address = new_address

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


class Transaction:
    def __init__(self, date_in, basket_in):
        self._date = date_in
        self._basket = basket_in

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


class Customer(Person):
    def __init__(self):
        self._basket = Basket()
        self._payment_details

    @property
    def basket(self):
        return self._basket

    @basket.setter
    def basket(self, new_basket):
        self._name = new_basket












person = Person('Aidan', 'Leeds')
print(person.name)
print(person.address)
person.username = 'red1809'
person.password = '123456'
print(person.password)
person.email = 'red@hotmail.com'
print(person.email)