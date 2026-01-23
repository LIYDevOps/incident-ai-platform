from fastapi import FastAPI
from controllers.incident_controller import router

app = FastAPI(title="Incident Service")

# Plug existing routes
app.include_router(router, prefix="/api/incidents")

@app.get("/health")
def health():
    return {"status": "UP"}
