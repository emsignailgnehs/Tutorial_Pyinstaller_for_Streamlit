import time

def write_counter(counter_field):
    with counter_field:
        counter_field.write(f'Time: {time.strftime("%H:%M:%S")}')
        time.sleep(1)