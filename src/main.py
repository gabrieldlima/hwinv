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
    # filled_slots = memory.get_memory_info()

    software_info = {
        "Operating System": operating_system_info
    }
    hardware_info = {
        "Computer":    computer_info,
        "Processor":   cpu_info,
        # "Memory":      filled_slots,
        # "Total Slots": total_slots,
        # "Empty Slots": empty_slots,
        "Disks":       disk_info,
        "Network":     network_info,
        "Graphics":    gpu_info,
    }

    with open(fr"{path}\software.json", "w", encoding="utf-8") as json_file:
        json.dump(software_info, json_file, indent=4)
    with open(fr"{path}\hardware.json", "w", encoding="utf-8") as json_file:
        json.dump(hardware_info, json_file, indent=4)


###############################################################################
# [[ Main function ]]
###############################################################################
def main():
    # directory_path = fr"Z:\TI\{socket.gethostname()}"
    directory_path = fr"output"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    export_to_json(directory_path)

if __name__ == "__main__":
    main()