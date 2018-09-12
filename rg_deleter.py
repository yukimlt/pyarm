import os,traceback,sys,threading,time
from modules import credential_set
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
sys.path.append("./loop/")
import rg_list

credentials, subscription_id = credential_set.get_credentials()
resource_client = ResourceManagementClient(credentials, subscription_id)

def delete_rg():
    print('\nDelete the Resource Group ...')
    delete_async_operation = resource_client.resource_groups.delete(GROUP_NAME_LIST)
    delete_async_operation.wait()

deleting = threading.Thread(target=delete_rg)
deleting.start()
