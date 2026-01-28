from fastapi import APIRouter

router = APIRouter()

@router.post("")
def create_incident(payload: dict):
    return {"status": "incident created", "payload": payload}

@router.post("/precheck")
def ai_precheck(payload: dict):
    hints = []

    title = payload.get("title", "").lower()
    description = payload.get("description", "").lower()
    priority = payload.get("priority")

    # Mandatory field checks
    if not payload.get("title"):
        hints.append("Title is mandatory.")

    if not payload.get("priority"):
        hints.append("Priority is mandatory.")

    if not payload.get("application_ci"):
        hints.append("Application CI is mandatory.")

    # Quality checks
    if len(payload.get("title", "")) < 5:
        hints.append("Title is too short. Please be more descriptive.")

    if len(description) < 15:
        hints.append("Description is too brief. Add more details.")

    # Priority intelligence (basic NLP)
    critical_keywords = ["down", "outage", "not working", "failure", "crash"]
    if any(word in description for word in critical_keywords):
        if priority not in ["P1", "P2"]:
            hints.append(
                "Issue sounds critical. Consider setting priority to P1 or P2."
            )

    return {
        "hints": hints,
        "hint_count": len(hints)
    }