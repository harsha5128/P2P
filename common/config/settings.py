from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServiceSettings(BaseSettings):
    service_name: str = "unknown-service"
    env: str = "dev"
    mongo_uri: str = "mongodb://localhost:27017"
    database_name: str = "p2p"
    openai_model: str = "gpt-4.1-mini"

    extract_url: str = Field(default="http://localhost:8001")
    validation_url: str = Field(default="http://localhost:8002")
    approval_url: str = Field(default="http://localhost:8003")
    sla_url: str = Field(default="http://localhost:8004")
    query_writer_url: str = Field(default="http://localhost:8005")

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False, extra="ignore")
