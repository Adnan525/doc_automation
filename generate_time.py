def generate_time(start_time, finish_time, patrol_times):

    current_time = start_time
    is_day_one = True
    check_if_23 = False
    check_if_0 = False

    # car patrol times conversion
    p_times = {
        "day_1" : [],
        "day_2" : []
    } 
    for val in patrol_times:
        # just one day so all patrol after 0000
        if int(val/100) == 0:
            check_if_0 = True
            check_if_23 = True
        else: 
            if int(val / 100) == 23:
                check_if_23 = True
            elif check_if_23 and int(val / 100) != 23:
                check_if_0 = True
        if check_if_0 and check_if_23:
            p_times["day_2"].append(val)
        else:
            p_times["day_1"].append(val)

    print(f"Patrol Times : {p_times}")
    # patrol activity
    times = {
        "day_1" : [start_time],
        "day_2" : []
    }

    while current_time != finish_time:
        current_time += 30

        # Handle the overflow to the next hour
        if current_time % 100 == 60:
            current_time += 40  # Add 40 minutes to handle overflow

        # Handle 0000
        if current_time == 2400:
            current_time = 0
            is_day_one = False
        
        current_time_str = str(current_time).zfill(4)
        current_time = int(current_time_str)
        
        if(is_day_one):
            times["day_1"].append(current_time)
        else:
            times["day_2"].append(current_time)
    print(f"External Patrol : {times}")

    # finish_time does not need to be added since we increment and then add it so it will go to 0130 then 0200; and then break
    
    # add 2 dictionaries
    # Concatenate the lists for each day
    day_1_combined = p_times['day_1'] + times['day_1']
    day_2_combined = p_times['day_2'] + times['day_2']

    # Sort the combined lists for each day
    sorted_day_1 = sorted(day_1_combined)
    sorted_day_2 = sorted(day_2_combined)

    # Create a new list containing both sorted results
    result_list = sorted_day_1 + sorted_day_2

    return [str(i).zfill(4) for i in result_list]


# ========another approach=================
# Assuming a threshold time (e.g., 0000) to decide between day 1 and day 2
# threshold_time = 1200

# day_1_patrol_times = [str(time).zfill(4) for time in patrol_times if time < threshold_time]
# day_2_patrol_times = [str(time).zfill(4) for time in patrol_times if time >= threshold_time]

# print("Day 1 Patrol Times:", day_1_patrol_times)
# print("Day 2 Patrol Times:", day_2_patrol_times)


# if __name__ == "__main__":
#     patrol_times = [2212,2345,2355,112,512]
#     print(generate_time(2200, 600, patrol_times))
#     # for val in patrol_times:
#     #     print(int(val/100))