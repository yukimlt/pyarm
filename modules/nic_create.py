from azure.mgmt.network import NetworkManagementClient
from . import variable_set

#variable.general_variable_set()
#variable.network_variable_set()

def create_nic(network_client):
    """Create a Network Interface for a VM.
    """
    # Create VNet
    print('\nCreate Vnet ...')
    async_vnet_creation = network_client.virtual_networks.create_or_update(
        variable_set.GROUP_NAME,
        variable_set.VNET_NAME,
        {
            'location': variable_set.LOCATION,
            'address_space': {
                'address_prefixes': ['10.0.0.0/16']
            }
        }
    )
    async_vnet_creation.wait()

    # Create Subnet
    print('\nCreate Subnet ...')
    async_subnet_creation = network_client.subnets.create_or_update(
        variable_set.GROUP_NAME,
        variable_set.VNET_NAME,
        variable_set.SUBNET_NAME,
        {'address_prefix': '10.0.0.0/24'}
    )
    subnet_info = async_subnet_creation.result()

    # Create public IP
    print('\nCreate Public IP ...')
    public_ip_addresses_params = {
        'location': variable_set.LOCATION,
        'public_ip_allocation_method': 'Dynamic'
    }
    async_ip_creation = network_client.public_ip_addresses.create_or_update(
        variable_set.GROUP_NAME,
        variable_set.IP_NAME,
        public_ip_addresses_params
    )
    ip_info = async_ip_creation.result()

    # Create NIC
    print('\nCreate NIC ...')
    publicIPAddress = network_client.public_ip_addresses.get(
        variable_set.GROUP_NAME,
        variable_set.IP_NAME
    )
    subnet_info = network_client.subnets.get(
        variable_set.GROUP_NAME,
        variable_set.VNET_NAME,
        variable_set.SUBNET_NAME
    )
    networkSecurityGroup = network_client.network_security_groups.get(
        variable_set.GROUP_NAME,
        variable_set.NSG_NAME
    )
    async_nic_creation = network_client.network_interfaces.create_or_update(
        variable_set.GROUP_NAME,
        variable_set.NIC_NAME,
        {
            'location': variable_set.LOCATION,
            'network_security_group': networkSecurityGroup,
            'ip_configurations': [{
                'name': variable_set.IP_CONFIG_NAME,
                'public_ip_address': publicIPAddress,
                'subnet': {
                     'id': subnet_info.id
                }
            }]
        }
    )
    return async_nic_creation.result()
