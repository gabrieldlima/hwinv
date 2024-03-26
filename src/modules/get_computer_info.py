import utils as u

###############################################################################
# [[ Get Computer information ]]
###############################################################################
def get_computer_info():
    computer_system = u.get_single_wmi_instance(u.W.Win32_ComputerSystemProduct)

    properties_map = {
        "IdentifyingNumber": "S/N",
        "Name": "Model",
        "Vendor": "Manufacturer"
    }

    computer_system_info = {}

    for prop in properties_map:
        value = getattr(computer_system, prop, None)
        if value is not None:
            computer_system_info[properties_map[prop]] = value

    return [computer_system_info]
