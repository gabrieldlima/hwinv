import utils as u

###############################################################################
# [[ Get Operating System information ]]
###############################################################################
def get_os_info():
    operating_system = u.get_single_wmi_instance(u.W.Win32_OperatingSystem)

    properties_map = {
        "Caption": "OS Name",
        "OSArchitecture": "OS Architecture",
        "Version": "OS Version",
        "InstallDate": "Install Date"
    }

    operating_system_info = {}

    for prop in properties_map:
        value = getattr(operating_system, prop, None)
        if value is not None:
            if prop == "InstallDate":
                operating_system_info[properties_map[prop]] = u.convert_date_format(value)
            else:
                operating_system_info[properties_map[prop]] = value

    return [operating_system_info]
