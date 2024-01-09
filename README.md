# Sample CDKTF Template

Template for using cdktf in Python in combination with pydantic for configuration management.

## Directory Structure

```
.
├── .env
├── cdktf.json
├── INFRA_CONFIG.yaml
├── Makefile
├── README.md
├── requirements.txt
└── src
    └── infra
        ├── config.py
        ├── deployer.py
        ├── infra_stack.py
        └── __init__.py
```



## Explanation

#### cdktf.json

Entry file for cdktf. The `app` key indicates which underlying python command to run for synthesizing / deploying the infrastructure code

#### INFRA_CONFIG.yaml

Configuration file for all non-secret parameters. This is parsed into pydantic config by `src/infra/config.py`

#### .env

Configuration file for all secret parameters. Do not check this into git. This is parsed together with `INFRA_CONFIG.yaml` into a pydantic config.

#### Makefile

Useful commands for infrastructure deployment.

#### src/infra/config.py

Pydantic model for all infrastructure parameters that are necessary to parametrize the deployment. Parameters are referenced by both `.env` for secrets and `INFRA_CONFIG.yaml`.

#### src/infra/deployer.py

Main entry file for cdktf commands. This connects the deployment stacks with pydantic configuration.

#### src/infra/infra_stack.py

File for infrastructure code. This can be separated into constructs in separate files for larger projects. Backend and provider are initialized here.

