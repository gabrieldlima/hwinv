import utils as u

###############################################################################
# [[ Get CPU information ]]
###############################################################################
def get_cpu_info():
    cpu = u.get_single_wmi_instance(u.W.Win32_Processor)

    properties_map = {
        "Architecture": "Arch",
        "Name": "Model",
        "NumberOfCores": "Cores",
        "NumberOfLogicalProcessors": "Threads",
    }

    cpu_info = {}

    for prop in properties_map:
        value = getattr(cpu, prop, None)
        if value is not None:
            if prop == "Architecture":
                if value == 9:
                    cpu_info[properties_map[prop]] = "x86_64"
                elif value == 0:
                    cpu_info[properties_map[prop]] = "x86_32"
                else:
                    cpu_info[properties_map[prop]] = "null"
            else:
                cpu_info[properties_map[prop]] = value

    return [cpu_info]
