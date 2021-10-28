### Error types used in the application

class PaymentError(Exception):
    pass

class ExpiryError(Exception):
    pass
  
class DatabaseError(Exception):
    pass
