import os
import traceback
import importlib
from modules import credential_set
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient

print ('create Azure Resource-Group\ntype the RG NAME')
GROUP_NAME=input('>>>  ')
USER_NAME=os.environ['USERNAME']

def run_rg_create():

    # Create all clients with an Application (service principal) token provider
    credentials, subscription_id = credential_set.get_credentials()
    resource_client = ResourceManagementClient(credentials, subscription_id)

    # Create Resource group
    print('\nCreate Resource Group ...')
    resource_client.resource_groups.create_or_update(
        '%s-%s' %(USER_NAME, GROUP_NAME),
        {
            'location': 'westus2'
        }
    )

if __name__ == "__main__":
    run_rg_create()
