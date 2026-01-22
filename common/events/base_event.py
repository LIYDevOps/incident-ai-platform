from abc import ABC
from datetime import datetime

class BaseEvent(ABC):
    def __init__(self, aggregate_id: str):
        self.aggregate_id = aggregate_id
        self.timestamp = datetime.utcnow()
