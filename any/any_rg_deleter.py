import os,traceback,sys,threading,time
from modules import credential_set
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient

print ('Delete Azure Resource-Group\ntype the Resource-Group NAME')
GROUP_NAME = input('>>>  ')

credentials, subscription_id = credential_set.get_credentials()
resource_client = ResourceManagementClient(credentials, subscription_id)

def delete_rg():
    print('\nDelete the Resource Group ...')
    delete_async_operation = resource_client.resource_groups.delete(GROUP_NAME)
    delete_async_operation.wait()

deleting = threading.Thread(target=delete_rg)
deleting.start()

while True:
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(1)
    if(not deleting.isAlive()):
        break
print('\nDeleted !: {}'.format(GROUP_NAME))
