from .base_event import BaseEvent

class IncidentCreatedEvent(BaseEvent):
    pass

class IncidentAssignedEvent(BaseEvent):
    def __init__(self, aggregate_id, assignment_group):
        super().__init__(aggregate_id)
        self.assignment_group = assignment_group
