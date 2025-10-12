from abc import ABC , abstractmethod




class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass


class VisaPayment(PaymentMethod):
    def pay(self,amount):
        print(f"Paying With {self.__class__.__name__} amount : {amount}")
    

class FawryPayment(PaymentMethod):
    def pay(self,amount):
        print(f"Paying With {self.__class__.__name__} amount : {amount}")


class OrderProcessor:
    def __init__(self,payment_method:PaymentMethod):
        self.payment_method = payment_method
    
    def checkout(self,amount):
        self.payment_method.pay(amount=amount)


OrderProcessor(VisaPayment()).checkout(amount=90)
OrderProcessor(FawryPayment()).checkout(amount=140)





