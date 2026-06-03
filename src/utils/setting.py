from pydantic_settings import SettingsConfigDict , BaseSettings

class Setting(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")
    DB_CONNECTION : str

setting = Setting()
