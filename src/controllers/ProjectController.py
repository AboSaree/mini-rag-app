from fastapi import UploadFile
from .BaseController import BaseController
from models.Enums import ResponseEnums
import os

class ProjectController(BaseController):
    def __init__(self):
        super().__init__()
    def get_project_dir(self, project_id:int):
        project_dir = os.path.join(self.files_dir, str(project_id))
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
        return project_dir