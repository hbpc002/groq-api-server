from pydantic_settings import BaseSettings
import json


class Settings(BaseSettings):
    groq_api_key: str = ""
    api_secret_token: str = "changeme-generate-a-real-token"
    default_model: str = "llama-3.3-70b-versatile"
    max_concurrent: int = 5
    request_timeout: int = 120
    enable_cors: bool = False
    cors_origins: str = "*"
    groq_base_url: str = "https://api.groq.com/openai/v1"
    max_messages_to_keep: int = 3
    
    model_settings: str = "{}"

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",")]
    
    @property
    def model_settings_dict(self) -> dict:
        try:
            return json.loads(self.model_settings)
        except:
            return {}

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
