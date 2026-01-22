from .base_ai_strategy import AIStrategy

class MandatoryFieldAI(AIStrategy):
    def predict(self, data):
        return {"description": 0.9, "ci": 0.3}
