from abc import ABC, abstractmethod
class pets(ABC):
    def receipt(self, amount):
        print("Kitten: ",amount)
# this function is telling us to pass an argument
    @abstractmethod
    def payment(self, amount):
        pass

class cardPayment(pets):
    #defined how to implement the payment function from its parent class, receipt
    def payment(self, amount):
        print('Your total comes to {} '.format(amount))

obj = cardPayment()
obj.receipt("$57")
obj.payment("$57")
