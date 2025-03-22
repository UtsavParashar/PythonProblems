from strategy import Strategy
from typing import List

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)

# when using Protocol interface, it is not necessary to inherit the abstract method from the interface   
class ConcreteStrategyB():
    def do_algorithm(self, data: List) -> List:
        return sorted(data, reverse=True)

