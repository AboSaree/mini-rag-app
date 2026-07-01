from fastapi import APIRouter, Depends, UploadFile,status
from helpers.config import Settings, get_settings
from controllers import DataController
from fastapi.responses import JSONResponse
from controllers import ProjectController
import os 
import aiofiles
from models.Enums import RespnoseEnums
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
    if not isvalid:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                             content={
                                 "isvalid": isvalid, "signal": signal
                                 })
    
    project_dir = ProjectController().get_project_dir(project_id=project_id)
    file_path = os.path.join(project_dir, file.filename)
    async with aiofiles.open(file_path, 'wb') as out_file:
        while content := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE_BYTES):
            await out_file.write(content)

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={
                            "isvalid": isvalid, "signal": signal
                        })