from enum import Enum
from datetime import datetime

class IncidentStatus(Enum):
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"
    REOPENED = "REOPENED"

class Incident:
    def __init__(self, id, short_desc, ci):
        self.id = id
        self.short_desc = short_desc
        self.ci = ci
        self.status = IncidentStatus.NEW
        self.assignment_history = []
        self.created_at = datetime.utcnow()
