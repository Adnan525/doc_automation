def generate_time(start_time, finish_time):
    times = [str(start_time).zfill(4)]
    current_time = start_time

    while current_time != finish_time:
        current_time += 30

        # Handle the overflow to the next hour
        if current_time % 100 == 60:
            current_time += 40  # Add 40 minutes to handle overflow

        # Handle 0000
        if current_time == 2400:
            current_time = 0
        
        current_time_str = str(current_time).zfill(4)
        current_time = int(current_time_str)
        times.append(current_time_str)

    # finish_time does not need to be added since we increment and then add it so it will go to 0130 then 0200; and then break

    return times

if __name__ == "__main__":
    start_time = 2200
    finish_time = 600

    generated_times = generate_time(start_time, finish_time)

    print("Generated Times:")
    for time in generated_times:
        print(time)
