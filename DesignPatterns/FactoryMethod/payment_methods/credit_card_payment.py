from .payment import Payment

class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print(f'Successfuly paid ${amount} using a Credit Card')