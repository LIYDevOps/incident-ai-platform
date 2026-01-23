from .base_sla_calculator import SLACalculator

class IncidentSLACalculator(SLACalculator):
    def calculate(self, events):
        return {"total_time": len(events)}
