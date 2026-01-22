from common.events.incident_events import IncidentCreatedEvent
from common.exceptions.domain_exception import DomainException

class IncidentService:
    def __init__(self, repo, event_bus, ai_client):
        self.repo = repo
        self.event_bus = event_bus
        self.ai = ai_client

    def create_incident(self, data):
        missing = self.ai.validate_fields(data)
        if missing:
            raise DomainException(f"Missing fields: {missing}")

        incident = self.repo.save(data)
        self.event_bus.publish(IncidentCreatedEvent(incident.id))
        return incident
