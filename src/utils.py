import wmi

###############################################################################
# [[ Initialize WMI object ]]
###############################################################################
W = wmi.WMI()

def get_all_wmi_instance(wmi_class):
    return wmi_class()

def get_single_wmi_instance(wmi_class):
    return wmi_class()[0]

def get_network_wmi_instance(wmi_class):
    return wmi_class()[1:3]

###############################################################################
# [[ Helper functions ]]
###############################################################################
def convert_bytes_to_megabytes(b):
    return int(b) / 1073741824

def convert_bytes_to_gigabytes(b):
    return int(b) / 1073741824

def convert_date_format(date_string):
    year = date_string[0:4]
    month = date_string[4:6]
    day = date_string[6:8]
    hour = date_string[8:10]
    minute = date_string[10:12]
    second = date_string[12:14]
    
    formatted_date = f"{day}/{month}/{year}, {hour}:{minute}:{second}"
    
    return formatted_date
