from abc import ABC, abstractmethod

class QualityRule(ABC):
    @abstractmethod
    def evaluate(self, incident):
        pass
