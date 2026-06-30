from fastapi import APIRouter, Depends, FastAPI
import os
from helpers.config import Settings, get_settings
base_router = APIRouter(
    prefix="/api/v1",
    tags = ["/api/v1"]
)
@base_router.get("/")
async def Welcome(app_settings: Settings = Depends(get_settings)):
    return {"message": f"Welcome to {app_settings.APP_NAME} v{app_settings.APP_VERSION}!"}