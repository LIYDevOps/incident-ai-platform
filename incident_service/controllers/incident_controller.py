from fastapi import APIRouter

router = APIRouter()

@router.post("")
def create_incident(payload: dict):
    return {"status": "incident created", "payload": payload}
