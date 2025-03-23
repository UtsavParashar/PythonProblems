from payment_factory import PaymentFactory

factory = PaymentFactory()
payment = factory.create('ApplePayment')
payment.pay(1000)