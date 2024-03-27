import utils as u

###############################################################################
# [[ Get Network information ]]
###############################################################################
def get_network_info():
    networks = u.get_all_wmi_instance(u.W.Win32_NetworkAdapter)

    properties_map = {
        "Description": "Description", 
        "MACAddress": "MAC Address", 
        "NetConnectionID": "Network Adapter",
    }  

    network_information_list = []

    for network in networks:
        network_information = {}
        description = getattr(network, "Description", None)
        if not u.check_string(description):
            for prop in properties_map:
                value = getattr(network, prop, None)
                if value is not None:
                    network_information[properties_map[prop]] = value
            network_information_list.append(network_information)

    return network_information_list
