from __future__ import annotations
from strategy import Strategy
from concrete_strategies import ConcreteStrategyA, ConcreteStrategyB


class Context:
    """ The Context defines the interface of interest to the clients """
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(['b', 'a', 'e', 'd', 'c'])
        print(','.join(result))

if __name__ == '__main__':
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    context.strategy = ConcreteStrategyB()
    print("Client: Strategy is set to reverse sorting.")
    context.do_some_business_logic()








