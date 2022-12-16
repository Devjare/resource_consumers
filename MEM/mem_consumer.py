import sys

def start_consuming():
    start_time = time.monotonic()

    while True: 
        current_time = time.monotonic()
        elapsed = current_time - start_time

        if  int(elapsed) % 5 == 0:
            UTILIZATION = int(os.getenv("UTILIZATION", "1"))
            set_consumption(UTILIZATION)
            time.sleep(1)

start_consuming
