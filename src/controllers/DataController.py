from fastapi import UploadFile
from .BaseController import BaseController
from models.Enums import ResponseEnums
import re 
import os

class DataController(BaseController):
    def __init__(self):
        super().__init__()


    def isValid(self,file:UploadFile):
        if (file.content_type not in self.settings.FILE_ALLOWED_TYPES):
            return False, ResponseEnums.INVALID_TYPE.value
        if (file.size > self.settings.FILE_MAX_SIZE_MB * 1024 * 1024):
            return False, ResponseEnums.SIZE_EXCEEDED.value
        return True, ResponseEnums.SUCCESS.value
    
    def generateUniqueFilePath(self, original_filename: str , project_id: str):
        # Replace spaces and special characters with underscores
        processed_filename = re.sub(r'[^\w\-_\.]', '_', original_filename)
        random_key = self.generateRandomKey()
        unique_filename = f"{processed_filename}_{random_key}"
        while os.path.exists(os.path.join(self.files_dir, project_id, unique_filename)):
            random_key = self.generateRandomKey()
            unique_filename = f"{processed_filename}_{random_key}"
        file_path = os.path.join(self.files_dir, project_id, unique_filename)
        return file_path , unique_filename
