from dotenv import load_dotenv
import os

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.env'))
load_dotenv(dotenv_path)  # Carga variables al entorno


from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='../../.env', extra='ignore')
    database_url: str
    debug: bool = False

settings = Settings()

print("DB URL:", settings.database_url)
print("Debug mode:", settings.debug)