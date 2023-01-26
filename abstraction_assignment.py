from abc import ABC, abstractmethod #abc module (Abstract Base Class)
class car(ABC):
    def paySlip(self,amount):
        print('Your purchase amount: ',amount)
# this function passes in an argument, but it's not yet defined
    @abstractmethod
    def payment(self,amount):
        pass

class DebitCardPayment(car):
# define how to implement payment function from parent class paySlip
    def payment(self,amount):
        print('Your pruchase amount of {} exceeded your $200 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip('$500')
obj.payment('$500')
# outputs paySlip string and obj value
# outputs payment string and obj value
