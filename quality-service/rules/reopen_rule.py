from .base_rule import QualityRule

class ReopenRule(QualityRule):
    def evaluate(self, incident):
        return max(0, 100 - incident.get("reopen_count", 0) * 20)
