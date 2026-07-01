from pydantic_settings import BaseSettings, SettingsConfigDict      
class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OpenAI_API_KEY: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE_MB: int
    FILE_DEFAULT_CHUNK_SIZE_BYTES: int

    class Config:
        env_file = ".env"
        
def get_settings() -> Settings:
    return Settings()