import utils as u

###############################################################################
# [[ Get Disk information ]]
###############################################################################
def get_disk_info():
    disks = u.get_all_wmi_instance(u.W.Win32_DiskDrive)

    properties_map = {
        "Model": "Model",
        "SerialNumber": "Serial Number",
        "Size": "Size",
    }

    disk_information_list = []

    for disk in disks:
        disk_information = {}
        for prop in properties_map:
            value = getattr(disk, prop, None)
            if value is not None:
                if prop == "Size":
                    gigabytes = u.convert_bytes_to_gigabytes(value)
                    disk_information[properties_map[prop]] = f"{gigabytes:.0f} GB"
                else:
                    disk_information[properties_map[prop]] = value
        disk_information_list.append(disk_information)

    return disk_information_list
