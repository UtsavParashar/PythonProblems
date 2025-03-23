from .payment import Payment

class NetBankingPayment(Payment):
    def pay(self, amount: float):
        print(f'Successfuly paid ${amount} using NetBanking')