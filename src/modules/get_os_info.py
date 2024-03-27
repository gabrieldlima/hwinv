import utils as u
import psutil

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

    operating_system_information_list = []

    os_info = {}
    for prop in properties_map:
        value = getattr(operating_system, prop, None)
        if value is not None:
            if prop == "InstallDate":
                os_info[properties_map[prop]] = u.convert_date_format(value)
            else:
                os_info[properties_map[prop]] = value
    operating_system_information_list.append(os_info)

    # Get disk usage from C: partition
    total, used, free, percent = psutil.disk_usage("C:")
    os_partition_usage = {
        "Total":   f"{u.convert_bytes_to_gigabytes(total):.0f} GB",
        "Used":    f"{u.convert_bytes_to_gigabytes(used):.0f} GB",
        "Free":    f"{u.convert_bytes_to_gigabytes(free):.0f} GB",
        "Percent": f"{percent}%",
    }
    os_partition_info = {
        "Local Disk (C:)": os_partition_usage
    }
    operating_system_information_list.append(os_partition_info)

    return operating_system_information_list
