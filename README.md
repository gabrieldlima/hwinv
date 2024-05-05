# Hardware and Software Information Gathering Tool for Windows Systems

This Python program enables users to gather detailed hardware and software information from Windows systems using the [Win32 Provider](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-provider). It provides comprehensive data on CPU, memory, disks, network adapters, operating system details, and more, outputting the results in JSON format for easy analysis and processing.

## Hardware Information
The hardware_info.json file contains detailed hardware information, including details on the computer, processor, memory, graphics, disk storage, and network adapters.
```json
{
    "COMPUTER": [
        {
            "S/N": "0000000",
            "Model": "OptiPlex Micro 7010",
            "Manufacturer": "Dell Inc."
        }
    ],
    "PROCESSOR": [
        {
            "Arch": "x86_64",
            "Model": "13th Gen Intel(R) Core(TM) i5-13500T",
            "Cores": 14,
            "Threads": 20
        }
    ],
    "MEMORY": [
        {
            "BankLabel": "DIMM0",
            "MemoryType": "DDR4",
            "FormFactor": "SODIMM",
            "Manufacturer": "KINGSTON",
            "Capacity": "16384 MB",
            "Speed": "3200 MHz"
        },
        {
            "Slots used": "1 of 2",
            "Size": "16 GB"
        }
    ],
    "GRAPHICS": [
        {
            "Model": "Intel(R) UHD Graphics 770"
        }
    ],
    "DISK": [
        {
            "Model": "KINGSTON SNV2S500G",
            "Serial Number": "0000_0000_0000",
            "Size": "466 GB"
        }
    ],
    "NETWORK": [
        {
            "Description": "Intel(R) Ethernet Connection (17) I219-LM",
            "MAC Address": "D0:94:66:E3:C0:5B",
            "Network Adapter": "Ethernet"
        },
        {
            "Description": "Intel(R) Wi-Fi 6E AX211 160MHz",
            "MAC Address": "F0:20:FF:C7:86:9D",
            "Network Adapter": "Wi-Fi"
        }
    ]
}
```
## Software information
The software_info.json file provides insights into the operating system and user details, including OS name, architecture, version, disk usage, and user information.
```json
{
    "OS": [
        {
            "OS Name": "Microsoft Windows 11 Pro",
            "OS Architecture": "64 bits",
            "OS Version": "10.0.22621",
            "Install Date": "27/03/2024, 14:02:06"
        },
        {
            "Local Disk (C:)": {
                "Total": "465 GB",
                "Used": "50 GB",
                "Free": "415 GB",
                "Percent": "10.8%"
            }
        }
    ],
    "USER": [
        {
            "Username": "DESKTOP-1VNS310\\User",
            "Domain": "WORKGROUP"
        }
    ]
}
```
