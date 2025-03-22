from abc import ABC, abstractmethod
from typing import List, Protocol

class Strategy(Protocol):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    def do_algorithm(self, data: List):
        pass