class QualityEngine:
    def __init__(self, rules):
        self.rules = rules

    def calculate(self, incident):
        scores = [r.evaluate(incident) for r in self.rules]
        return sum(scores) / len(scores)
