def collect_data():
    serial_no = input("Enter Report Serial no. ")
    officer_name = input("Enter Security Officer's name: ")
    replaced_officer = input("Enter Replacing Security Officer's name: ")
    license_no = input("Enter License No.: ")
    start_time = int(input("Enter Start time (24-hour format): "))
    finish_time = int(input("Enter Finish time (24-hour format): "))
    patrol_times_string = input("Enter Patrol times ('-' separated integers, e.g., 2230-2312-0050): ")
    patrol_times = [int(time.strip()) for time in patrol_times_string.split('-')]

    return {
        "serial_no" : serial_no,
        "officer_name": officer_name,
        "replaced_officer" : replaced_officer,
        "license_no": license_no,
        "start_time": start_time,
        "finish_time": finish_time,
        "patrol_times": patrol_times
    }

def collect_data_master():
    data = input("Enter details as serialNo<s>replaced<s>starTime<s>finishTime<s>patrol-time : ")
    data = data.split(" ")

    return {
        "serial_no" : data[0],
        "officer_name": "Muntasir Adnan",
        "replaced_officer" : data[1],
        "license_no": "17728013",
        "start_time": int(data[2]),
        "finish_time": int(data[3]),
        "patrol_times": [int(time.strip()) for time in data[4].split("-")]
    }