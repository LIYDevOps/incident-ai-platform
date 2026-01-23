from fastapi import APIRouter

router = APIRouter()

@router.post("/incidents")
def create_incident(payload: dict):
    return {"status": "incident created", "payload": payload}
