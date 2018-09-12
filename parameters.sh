#!/bin/sh
#This script set parameters for vm_creator.py & rg_deleter.py

# set credential(your service principal ID)
export AZURE_TENANT_ID=
export AZURE_CLIENT_ID=
export AZURE_CLIENT_SECRET=
export AZURE_SUBSCRIPTION_ID=

# set user(this is your VM's user name and header of resource-group's name )
export JBS_USERNAME=

# set your ssh public key (raw data)
export PUBLIC_KEY=''

# set VM's OS, you can chose following OS type
# "ubuntu16", "ubuntu18", "centos", "rhel" (both centos & rhel are version 7)
export AZURE_VM_OS=

# set VM size
export AZURE_VM_SIZE=
