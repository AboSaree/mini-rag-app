from fastapi import UploadFile
from .BaseController import BaseController
from models.Enums import ResponseEnums

class DataController(BaseController):
    def __init__(self):
        super().__init__()
    def isValid(self,file:UploadFile):
        if (file.content_type not in self.settings.FILE_ALLOWED_TYPES):
            return False, ResponseEnums.INVALID_TYPE.value
        if (file.size > self.settings.FILE_MAX_SIZE_MB * 1024 * 1024):
            return False, ResponseEnums.SIZE_EXCEEDED.value
        return True, ResponseEnums.SUCCESS.value
