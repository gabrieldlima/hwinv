# NOTE: https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-provider

import os
import json
import socket
from modules import get_cpu_info as cpu
from modules import get_memory_info as memory
from modules import get_gpu_info as gpu
from modules import get_disk_info as disk
from modules import get_network_info as network
from modules import get_computer_info as computer
from modules import get_os_info as operatingsystem
from modules import get_username_info as username


###############################################################################
# [[ Export software/hardware info to JSON ]]
###############################################################################
def export_to_json(path):
    operating_system_info                  = operatingsystem.get_os_info()
    computer_info                          = computer.get_computer_info()
    cpu_info                               = cpu.get_cpu_info()
    disk_info                              = disk.get_disk_info()
    network_info                           = network.get_network_info()
    gpu_info                               = gpu.get_gpu_info()
    memory_info                            = memory.get_memory_info()
    username_info                          = username.get_username_info()

    software_info = {
        "OS":   operating_system_info,
        "USER": username_info,
    }
    hardware_info = {
        "COMPUTER":    computer_info,
        "PROCESSOR":   cpu_info,
        "MEMORY":      memory_info,
        "GRAPHICS":    gpu_info,
        "DISK":        disk_info,
        "NETWORK":     network_info,
    }

    with open(fr"{path}\software_info.json", "w", encoding="utf-8") as json_file:
        json.dump(software_info, json_file, indent=4)
    with open(fr"{path}\hardware_info.json", "w", encoding="utf-8") as json_file:
        json.dump(hardware_info, json_file, indent=4)


###############################################################################
# [[ Main function ]]
###############################################################################
def main():
    directory_path = fr"Z:\TI\INVENTARIO\{socket.gethostname()}"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    export_to_json(directory_path)

if __name__ == "__main__":
    main()