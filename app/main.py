from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.users import router as users_router


app = FastAPI(
    title="HireFlow API",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {"message": "HireFlow API is running"}


app.include_router(health_router)
app.include_router(users_router)