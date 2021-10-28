"""Contains strings and regex patterns that are called from various routes in
    the main application and from the classes and unittest files."""
import re

SUCCESSFUL_PAYMENT_MESSAGE = 'Thank you, your payment was successful.'
NON_EXISTENT_DETAILS_MESSAGE = 'Payment declined. These details do not exist in our database.'
UPDATED_CATALOGUE_MESSAGE = 'Your catalogue has been updated'
UPDATED_STOREFRONT_MESSAGE = 'Your storefront has been updated'
PAYMENT_DECLINED = 'Payment declined'
INVALID_LOGIN = 'Invalid username and/or password'

CARD_REGEX = re.compile(r'[\d]{16}')
SORT_CODE_REGEX = re.compile(r'[\d]{6}')
CVV_REGEX = re.compile(r'[\d]{3}')
EMAIL_REGEX = re.compile(r'[\w]*@[\w]*\.[\w]*')
ONLINE_SERVICE_NUMBER_REGEX = re.compile(r'[\d]{4}')
STOREFRONT_REGEX = re.compile(r'.*\.(png|PNG|jpeg|JPEG)')

DATE_FORMAT = "%Y-%m-%d"

PAYMENT_TYPES = ['CARD', 'ONLINE']
CARD_TYPES = ['VISA', 'MASTERCARD', 'AMEX']
DELIVERY_TYPES = ['FIRST CLASS', 'SECOND CLASS', 'COURIER']