from helpers.config import Settings, get_settings

class BaseController:
    def __init__(self):
        self.settings: Settings = get_settings()