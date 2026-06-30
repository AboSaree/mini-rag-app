from fastapi import APIRouter, Depends, UploadFile
from helpers.config import Settings, get_settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data", 
    tags = ["/api/v1"]
)

@data_router.post("/upload/{project_id}")
async def upload_file(
    project_id: int,
    file: UploadFile,
    app_settings: Settings = Depends(get_settings),
):
    controller = DataController()
    isvalid, signal = controller.isValid(file=file)
    return {"isvalid": isvalid, "signal": signal}