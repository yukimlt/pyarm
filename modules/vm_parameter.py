from . import variable_set

def create_vm_parameters(nic_id, vm_reference):
    """Create the VM parameters structure.
    """
    return {
        'location': variable_set.LOCATION,
        'os_profile': {
            'computer_name': variable_set.VM_NAME,
            'admin_username': variable_set.USER_NAME,
            'linux_configuration': {
                'disable_password_authentication': True,
                'ssh': {
                    'public_keys': [{
                        'path': '/home/{}/.ssh/authorized_keys'.format(variable_set.USER_NAME),
                        'key_data': variable_set.PUBLIC_KEY
                    }]
                }
            }
        },
        'hardware_profile': {
            'vm_size': variable_set.VM_SIZE
        },
        'storage_profile': {
            'image_reference': {
                'publisher': vm_reference['publisher'],
                'offer': vm_reference['offer'],
                'sku': vm_reference['sku'],
                'version': vm_reference['version']
            },
        },
        'network_profile': {
            'network_interfaces': [{
                'id': nic_id,
            }]
        },
    }
