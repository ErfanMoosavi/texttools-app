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


settings = Settings()
