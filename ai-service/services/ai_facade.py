class AIFacade:
    def __init__(self, strategies: dict):
        self.strategies = strategies

    def validate_fields(self, data):
        scores = self.strategies["mandatory"].predict(data)
        return [k for k, v in scores.items() if v < 0.6]
