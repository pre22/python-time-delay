import time

def time_delay(seconds):
    current_time = time.time()
    target_time = current_time + seconds

    while time.time() < target_time:
        pass

    return True