from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BASE_URL: str
    KINOPOISK_API_KEY: str
        
    model_config = SettingsConfigDict(
        env_file=".env.docker",
        extra="ignore"
    )
    
Config = Settings()