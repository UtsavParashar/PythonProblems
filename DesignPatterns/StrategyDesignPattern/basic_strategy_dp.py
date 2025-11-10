# When there are more than one way/algos/behaviors to do a task, we can use Strategy Design pattern.
# Strategy dp is of behavioral type - as it allows to define the more than one behaviors 
# Basic Structure - 
# 1. Behavior Interface
# 2. Algos concrete classes
# 3. Context Class - When helps set/apply the strategy at runtime
# 4. Client code

# Benefits - 
# Provides the ability to choose one of the many algos/strategies at runtime
# Avoid clumsy if-else statements to choose behavior
# Extensibility is easy
# Failure of one algo does not affect another algo 
# Follows Open Close and Single responsibility principle
# Promotes code reuseability and flexibility
# Makes algorithms interchangeable and easier to test independently
 
# Downsides 
# Each algo is to be written in a separate class
# The client must understand the difference between strategies to choose correctly


from abc import ABC, abstractmethod

# Interface
class TradingStrategy(ABC):
    @abstractmethod
    def execute(self, quantity: int) -> None:
        pass

# Algo's/behaviors --> TWAP, VWAP, Active(Market Order), Passive(Limit Order)
class TWAPStrategy(TradingStrategy):
    def execute(self, quantity: int) -> None:
        print(f'Applying {self.__class__.__name__} for quantity - {quantity}')


class VWAPStrategy(TradingStrategy):
    def execute(self, quantity: int) -> None:
        print(f'Applying {self.__class__.__name__} for quantity - {quantity}')

# Extending to Passive orders
class PassiveStrategy(TradingStrategy):
    def execute(self, quantity: int) -> None:
        print(f'Applying {self.__class__.__name__} for quantity - {quantity}')


# Context Class
class TradingStrategyContext:
    def __init__(self, strategy: TradingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: TradingStrategy) -> None:
        if not isinstance(strategy, TradingStrategy):
            raise TypeError('strategy must be an instance of TradingStrategy')
        self._strategy = strategy

    def execute_strategy(self, quantity) -> None:
        self._strategy.execute(quantity)

# Client Code
execution_strategy = TradingStrategyContext(TWAPStrategy())
execution_strategy.execute_strategy(10)

execution_strategy.set_strategy(VWAPStrategy())
execution_strategy.execute_strategy(10)

execution_strategy.set_strategy(PassiveStrategy())
execution_strategy.execute_strategy(10)