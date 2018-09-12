import os,traceback,importlib,csv
from modules import credential_set
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient

GROUP_NAME=input('>>>  ')
USER_NAME=os.environ['USERNAME']

with open('./loop/group_list.csv', newline='') as f:
    goruplist = list(csv.reader(f))

def run_any_rg_create():

    # Create all clients with an Application (service principal) token provider
    credentials, subscription_id = credential_set.get_credentials()
    resource_client = ResourceManagementClient(credentials, subscription_id)

    # Create Resource group
    print('\nCreate Resource Group ...')

    for s in grouplist:
        resource_client.resource_groups.create_or_update(
            '%s-%s' %(USER_NAME, s),
            {
                'location': 'westus2'
                }
        )

if __name__ == "__main__":
    run_any_rg_create()
