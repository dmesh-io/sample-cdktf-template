from cdktf import AzurermBackend, TerraformStack
from cdktf_cdktf_provider_azurerm.provider import (
    AzurermProvider,
    AzurermProviderFeatures,
)
from cdktf_cdktf_provider_azurerm.storage_account import StorageAccount
from cdktf_cdktf_provider_azurerm.storage_container import StorageContainer
from constructs import Construct

from infra.config import InfraConfig


class InfraStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: InfraConfig):
        super().__init__(scope, id)

        self.config = config

        self.initialize_backend()
        self.initialize_provider()

        # define resources here e.g.
        self.storage_account = StorageAccount(
            scope=self,
            id_="template_storage_account",
            name="templatestoacc123",
            resource_group_name=self.config.resource_group_name,
            location=self.config.azure_location,
            account_tier="Standard",
            account_replication_type="LRS"
        )

        self.data_container = StorageContainer(
            scope=self,
            id_="template_storage_container",
            storage_account_name=self.storage_account.name,
            name="data_container"
        )


    def initialize_backend(self):
        AzurermProvider(
            scope=self,
            id="Azurerm",
            client_id=self.config.arm_client_id,
            client_secret=self.config.arm_client_secret,
            features=AzurermProviderFeatures(),
            subscription_id=self.config.arm_subscription_id,
            tenant_id=self.config.arm_tenant_id,
        )

    def initialize_provider(self):
        AzurermBackend(
            scope=self,
            subscription_id=self.config.arm_subscription_id,
            tenant_id=self.config.arm_tenant_id,
            resource_group_name=self.config.backend_resource_group,
            storage_account_name=self.config.backend_storage_account,
            container_name=self.config.backend_container_name,
            key=self.config.backend_storage_key,
            client_id=self.config.arm_client_id,
            client_secret=self.config.arm_client_secret,
        )
