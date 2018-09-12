import os
import traceback
import importlib
import modules
from modules import variable_set
from modules import nic_create
from modules import vm_parameter
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption
from azure.mgmt.storage.models import (
    StorageAccountCreateParameters,
    StorageAccountUpdateParameters,
    Sku,
    SkuName,
    Kind
)
from azure.mgmt.network.v2017_03_01.models import NetworkSecurityGroup
from azure.mgmt.network.v2017_03_01.models import SecurityRule
from msrestazure.azure_exceptions import CloudError

def run_vm_create():

    # Create all clients with an Application (service principal) token provider
    credentials, subscription_id = modules.credential_set.get_credentials()
    resource_client = ResourceManagementClient(credentials, subscription_id)
    compute_client = ComputeManagementClient(credentials, subscription_id)
    network_client = NetworkManagementClient(credentials, subscription_id)
    storage_client = StorageManagementClient(credentials, subscription_id)

    # Create Resource group
    print('\nCreate Resource Group ...')
    resource_client.resource_groups.create_or_update(
        variable_set.GROUP_NAME,
        {
            'location': variable_set.LOCATION
        }
    )

    # Create Storage account
    print('\nCreate Storage Account ...')
    storage_async_operation = storage_client.storage_accounts.create(
        variable_set.GROUP_NAME,
        variable_set.STORAGE_ACCOUNT_NAME,
        StorageAccountCreateParameters(
            sku=Sku(SkuName.standard_lrs),
            kind=Kind.storage,
            location=variable_set.LOCATION
        )
    )
    storage_account = storage_async_operation.result()

    # Create Network Security Group
    print('\nCreate Network Security Group ...')
    nsg_params = NetworkSecurityGroup()
    nsg_params.location = variable_set.LOCATION
    nsg_params.security_rules = [
        SecurityRule('Tcp', '*', '*', 'Allow', 'Inbound', description='',
                     source_port_range='*', destination_port_range='22', priority=1000, name='default-allow-ssh')
    ]

    nsg_async_operation = network_client.network_security_groups.create_or_update(
        variable_set.GROUP_NAME,
        variable_set.NSG_NAME,
        nsg_params
    )

    try:
        # Create a NIC
        nic = nic_create.create_nic(network_client)

        # Create VM
        print('\nCreate Virtual Machine ...')
        vm_parameters = vm_parameter.create_vm_parameters(
            nic.id,
            variable_set.VM_REFERENCE['%s' % variable_set.COMPUTE]
        )
        async_vm_creation = compute_client.virtual_machines.create_or_update(
            variable_set.GROUP_NAME,
            variable_set.VM_NAME,
            vm_parameters
        )
        async_vm_creation.wait()

        # Start VM
        print('\nStart VM ...')
        async_vm_start = compute_client.virtual_machines.start(
            variable_set.GROUP_NAME,
            variable_set.VM_NAME
        )
        async_vm_start.wait()

    except CloudError:
        print('A VM operation failed:', traceback.format_exc(), sep='\n')
    else:
        print('All operations completed successfully!')

if __name__ == "__main__":
    run_vm_create()
