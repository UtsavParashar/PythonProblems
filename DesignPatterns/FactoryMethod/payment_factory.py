from inspect import getmembers, isclass, isabstract
import payment_methods

class PaymentFactory:

    def __init__(self):
        self.payment_implementations = {}
        self._load_payment_methods()

    def _load_payment_methods(self):
        implementations = getmembers(payment_methods, lambda m: isclass(m) and not isabstract(m))
        for name, _type in implementations:
            if isclass(_type) and issubclass(_type, payment_methods.Payment):
                self.payment_implementations[name] = _type


    def create(self, payment_type: str):
        if payment_type in self.payment_implementations:
            return self.payment_implementations[payment_type]()
        else:
            raise ValueError(f'{payment_type} type is not currently supported as a payment method')













# if __name__ == '__main__':
#     PaymentFactory().load_payment_methods()
