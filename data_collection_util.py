def collect_data():
    officer_name = input("Enter Security Officer's name: ")
    replaced_officer = input("Enter Replaced Security Officer's name: ")
    license_no = input("Enter License No.: ")
    start_time = int(input("Enter Start time (24-hour format): "))
    finish_time = int(input("Enter Finish time (24-hour format): "))
    patrol_times_string = input("Enter Patrol times (comma-separated integers, e.g., 2200,2300,0100): ")
    patrol_times = [int(time.strip()) for time in patrol_times_string.split(',')]

    return {
        "officer_name": officer_name,
        "replaced_officer" : replaced_officer,
        "license_no": license_no,
        "start_time": start_time,
        "finish_time": finish_time,
        "patrol_times": patrol_times
    }

def collect_data_master():
    data = input("Enter details as replaced<s>starTime<s>finishTime<s>patrol-time : ")
    data = data.split(" ")

    return {
        "replaced_officer" : data[0],
        "start_time": int(data[1]),
        "finish_time": int(data[2]),
        "patrol_times": [int(time.strip()) for time in data[3].split("-")]
    }