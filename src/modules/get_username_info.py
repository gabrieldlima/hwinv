import utils as u

###############################################################################
# [[ Get username/domain information ]]
###############################################################################
def get_username_info():
    wmi_class = u.get_single_wmi_instance(u.W.Win32_ComputerSystem)

    properties_map = {
        "UserName": "Username",
        "Domain": "Domain"
    }

    wmi_class_info = {}

    for prop in properties_map:
        value = getattr(wmi_class, prop, None)
        if value is not None:
            wmi_class_info[properties_map[prop]] = value

    return [wmi_class_info]