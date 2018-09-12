# PYthon Azure Resource Manager
verified by ubuntu16.04 and python 3.5
## what's this ?
Python Azure Resource Manager (pyarm) create VM, and delete Resource-Group on Microsoft Azure by python.
```
pyarm/
  ├ modules/
  |    ├ __pycache__/
  │    ├ __init__.py
  │    ├ credential_set.py
  │    ├ nic_create.py
  │    ├ variable_set.py
  │    └ vm_parameter.py
  ├ env.list
  ├ parameters.sh
  ├ rg_deleter.py
  └ vm_creator.py
```
## before you begin
- install python3, pip3
- install python modules

    ```
    $ apt-get -y install python3 curl
    $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $ python3 get-pip.py
    $ pip3 install azure==3.0.0
    $ pip install keyrings.alt
    ```
- service principal id  
if you don't have available service_principal_id, create it.  
https://docs.microsoft.com/ja-jp/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest
```
$ az ad sp create-for-rbac -n "http://<<YOUR_SERVICE_PRINCIPAL_NAME>>" --role contributor > service_principal_id
```
- ssh public key  
You should use public ssh key for access to VM on Azure. So this key is necessary that belongs to PC you want to connect to VM.
if you don't have it, to generate.

## how to use
env set for vm parameters  

parameters.sh
```sh
#!/bin/sh
#This script set parameters for vm_creator.py & rg_deleter.py

# set credential(your service principal ID)
export AZURE_TENANT_ID=YOUR_SERVICE_PRINCIPAL_TENANT
export AZURE_CLIENT_ID=YOUR_SERVICE_PRINCIPAL_APPID
export AZURE_CLIENT_SECRET=YOUR_SERVICE_PRINCIPAL_PASSWORD
export AZURE_SUBSCRIPTION_ID=YOUR_AZURE_SUBSCRIPTION_ID

# set user(this is your VM's user name and header of resource-group's name )
export JBS_USERNAME=

# set your ssh public key (raw data)
export PUBLIC_KEY='ssh-rsa ...'

# set VM's OS, you can chose following OS type
# "ubuntu16", "ubuntu18", "centos", "rhel" (both centos & rhel are version 7)
export AZURE_VM_OS=ubuntu16

# set VM size
export AZURE_VM_SIZE=Basic_A0
```
set parameters
```
$ source ./parameter.sh
```
create vm
```
yuki@DevHost2:~/py_sandbox$ python3 vm_creator.py
create VritualMachine on Azure
type the VM NAME
>>>  test

Create Resource Group ...

Create Storage Account ...

Create Network Security Group ...

Create Vnet ...

Create Subnet ...

Create Public IP ...

Create NIC ...

Create Virtual Machine ...

Start VM ...
All operations completed successfully!
```
delete resource-group
```
yuki@DevHost2:~/py_sandbox$ python3 rg_deleter.py
Delete Azure Resource-Group
type the Resource-Group NAME
>>>  yuhirose-test

Deleting the Resource Group....
.........................................................................................................
Deleted !: yuhirose-test
```
## by docker
```
yuki@Docker:~$ docker run --name creator -it --env-file env.list pyarm:0704
create VritualMachine on Azure
type the VM NAME
>>>  hogehuga

Create Resource Group ...

Create Storage Account ...

Create Network Security Group ...

Create Vnet ...

Create Subnet ...

Create Public IP ...

Create NIC ...

Create Virtual Machine ...

Start VM ...
All operations completed successfully!
```

## improvements
- pyarm don't create auto shutdown
    - python azure sdk can't create that. (TBC)
- hostname
    - you can use only lower-case letters at VM's hostname because it use storage acount name too.
- username
    - pyarm using username for resource-group-name's header. that's not my favorite, i'm planning to separate.
