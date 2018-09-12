import os

print ('create VritualMachine on Azure\ntype the VM NAME')
VM_NAME = input('>>>  ')
VM_SIZE = os.environ['AZURE_VM_SIZE']
USER_NAME = os.environ['USERNAME']
LOCATION = 'westus2'
GROUP_NAME = '%s-%s' %(USER_NAME, VM_NAME)
COMPUTE = os.environ['AZURE_VM_OS']
PUBLIC_KEY = os.environ['PUBLIC_KEY']
VM_REFERENCE = {
    'ubuntu16': {
        'publisher': 'Canonical',
        'offer': 'UbuntuServer',
        'sku': '16.04.0-LTS',
        'version': 'latest'
    },
    'ubuntu18': {
        'publisher': 'Canonical',
        'offer': 'UbuntuServer',
        'sku': '18.04.0-LTS',
        'version': 'latest'
    },
    'centos': {
        'publisher': 'OpenLogic',
        'offer': 'CentOS',
        'sku': '7.3',
        'version': 'latest'
    },
    'rhel': {
        'publisher': 'RedHat',
        'offer': 'RHEL',
        'sku': '7.3',
        'version': 'latest'
    }
}

VNET_NAME = '%s-vnet' % GROUP_NAME
SUBNET_NAME = '%s-subnet' % GROUP_NAME
IP_NAME = '%s-ip' % VM_NAME
NSG_NAME = '%s-nsg' % VM_NAME
IP_CONFIG_NAME = '%s-ip-config' % VM_NAME
NIC_NAME = '%s-nic' % VM_NAME

OS_DISK_NAME = 'azure-sample-osdisk'
STORAGE_ACCOUNT_NAME = '%s%sdisks' %(USER_NAME, VM_NAME)
