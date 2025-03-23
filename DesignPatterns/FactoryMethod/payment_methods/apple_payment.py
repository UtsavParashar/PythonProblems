from .payment import Payment

class ApplePayment(Payment):
    def pay(self, amount: float):
        print(f'Successfuly paid ${amount} using Apple Pay')