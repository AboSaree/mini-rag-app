from fastapi import APIRouter, Depends, UploadFile,status
from helpers.config import Settings, get_settings
from controllers import DataController
from fastapi.responses import JSONResponse
from controllers import ProjectController
import os 
import aiofiles
from models.Enums import RespnoseEnums
import logging 

logger = logging.getLogger("uvicorn errors")

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
    file_path,file_id = controller.generateUniqueFilePath(original_filename=file.filename, project_id=str(project_id))

    try:
        async with aiofiles.open(file_path, 'wb') as out_file:
            while content := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE_BYTES):
                await out_file.write(content)
    except Exception as e:
        logger.error(f"Error saving file: {e}")
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={
                                "isvalid": False, 
                                "signal":RespnoseEnums.FILE_SAVE_ERROR.value
                            })

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={
                            "isvalid": isvalid,
                            "signal": signal,
                            "file_id": file_id,
                        })