from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App info
    title: str = "TextTools API"
    version: str = "0.1.0"
    description: str = "A simple API for TextTools"
    contact: dict[str, str] = {
        "name": "Erfan Moosavi",
        "email": "erfanmoosavi84@gmail.com",
    }
    license_info: dict[str, str] = {"name": "MIT"}

    # LLM API settings
    base_url: str
    api_key: str
    llm_model: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


settings = Settings()
