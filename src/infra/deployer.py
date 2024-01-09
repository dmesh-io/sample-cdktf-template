import os
from pathlib import Path

from cdktf import App

from infra.config import get_config
from infra.infra_stack import InfraStack

root_dir = Path(__file__).parent.parent.parent


def main():
    app = App()

    config_path = os.environ.get(
        "CDKTF_INFRA_CONFIG", root_dir / "INFRA_CONFIG.yaml"
    )
    config = get_config(config_path)

    InfraStack(app, "infra-stack", config=config)

    app.synth()


if __name__ == "__main__":
    main()
