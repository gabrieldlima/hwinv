import utils as u

###############################################################################
# [[ Get information about physical memory (DIMMs) ]]
###############################################################################
def get_memory_info():
    memory = u.get_all_wmi_instance(u.W.Win32_PhysicalMemory)

    properties_map = {
        "BankLabel": "BankLabel", 
        "MemoryType": "MemoryType",
        "FormFactor": "FormFactor",
        "Manufacturer": "Manufacturer",
        "Capacity": "Capacity",
        "Speed": "Speed"
    }

    memory_information_list = []

    memory_total = 0

    for mem in memory:
        slot_information = {}
        for prop in properties_map:
            value = getattr(mem, prop, None)
            if value is not None:
                if prop == "MemoryType":
                    # DDR (20), DDR2 (21), DDR3 (24), DDR3L (25), DDR4 (26)
                    if value == 20:
                        slot_information[properties_map[prop]] = f"DDR"
                    elif value == 21:
                        slot_information[properties_map[prop]] = f"DDR2"
                    elif value == 24:
                        slot_information[properties_map[prop]] = f"DDR3"
                    elif value == 25:
                        slot_information[properties_map[prop]] = f"DDR3L"
                    elif value == 26:
                        slot_information[properties_map[prop]] = f"DDR4"
                    else:
                        slot_information[properties_map[prop]] = value
                elif prop == "FormFactor":
                    # DIMM (3), SODIMM (12)
                    if value == 8:
                        slot_information[properties_map[prop]] = f"DIMM"
                    elif value == 12:
                        slot_information[properties_map[prop]] = f"SODIMM"
                    elif value == 0:
                        slot_information[properties_map[prop]] = f"Unknown"
                    else:
                        slot_information[properties_map[prop]] = value
                elif prop == "Capacity":
                    memory_total += int(value)
                    megabytes = u.convert_bytes_to_megabytes(value)
                    slot_information[properties_map[prop]] = f"{megabytes:.0f} MB"
                elif prop == "Speed":
                    slot_information[properties_map[prop]] = f"{value} MHz"
                else:
                    slot_information[properties_map[prop]] = value
        memory_information_list.append(slot_information)


    # [[ Get total number of slots, including filled slots and empty slots ]]
    memory_array = u.get_single_wmi_instance(u.W.Win32_PhysicalMemoryArray)
    total_slots = getattr(memory_array, "MemoryDevices", None)
    slots_used = {
        "Slots used": f"{len(memory)} of {total_slots}",
        "Size": f"{u.convert_bytes_to_gigabytes(memory_total):.0f} GB"
    }
    memory_information_list.append(slots_used)

    return memory_information_list