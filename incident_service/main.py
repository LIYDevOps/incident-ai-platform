from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from incident_service.controllers.incident_controller import router

app = FastAPI(title="Incident Service")

# Cors middleware (for UI access)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # Need to restrict on production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Plug existing routes
app.include_router(router, prefix="/api/incidents")

@app.get("/health")
def health():
    return {"status": "UP"}
