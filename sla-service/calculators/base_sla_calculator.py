from abc import ABC, abstractmethod

class SLACalculator(ABC):
    @abstractmethod
    def calculate(self, events):
        pass
