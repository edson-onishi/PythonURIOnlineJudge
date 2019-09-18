time_seconds = int(input())

def format_time(seconds):

    hours = seconds / 3600
    remaining_seconds = seconds - hours * 3600
    minutes = remaining_seconds / 60
    seconds = remaining_seconds - minutes * 60

    return hours, minutes, seconds

print("{}:{}:{}".format(*format_time(time_seconds)))