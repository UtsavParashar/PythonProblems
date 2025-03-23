from .payment import Payment

class UPIPayment(Payment):
    def pay(self, amount: float):
        print(f'Successfuly paid ${amount} using UPI')