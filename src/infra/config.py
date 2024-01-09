from pathlib import Path

import yaml
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class InfraConfig(BaseSettings):
    arm_tenant_id: str
    arm_subscription_id: str
    arm_client_id: str
    arm_client_secret: str
    backend_storage_account: str
    backend_storage_container: str
    backend_storage_account_key: str


def get_config(path: Path) -> InfraConfig:
    # this loads secrets from parent .env file:
    load_dotenv()

    with open(path, "r") as f:
        config_dict = yaml.safe_load(f)

        infra_config = InfraConfig(**config_dict)

    return infra_config
