from helpers.config import Settings, get_settings
import os 
import random
import string
class BaseController:
    def __init__(self):
        self.settings: Settings = get_settings()
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.files_dir = os.path.join(self.base_dir, "assets", "files")

        
    def generateRandomKey(self, length: int = 8) -> str:
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))