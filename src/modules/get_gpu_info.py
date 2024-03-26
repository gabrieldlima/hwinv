import utils as u

###############################################################################
# [[ Get GPU information ]]
###############################################################################
def get_gpu_info():
    gpus = u.get_all_wmi_instance(u.W.Win32_VideoController)

    properties_map = {
        "Description": "Model",
    }

    gpu_information_list = []

    for gpu in gpus:
        gpu_information = {}
        for prop in properties_map:
            value = getattr(gpu, prop, None)
            if value is not None:
                gpu_information[properties_map[prop]] = value
        gpu_information_list.append(gpu_information)

    return gpu_information_list
