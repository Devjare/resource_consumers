import sys
import os
from flask import Flask, request
import time
import numpy as np
from threading import Thread

app = Flask(__name__)
MAX_OPERATIONS = int(os.getenv("MAX_OPERATIONS", "8"))
INTERVAL = int(os.getenv("INTERVAL", "8"))

def bubble_sort(size):
    """
    Function to create a random array of size 'size'
    and sort with bubble sort
    """
    arr = np.random.random(size)
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr

sorting_queue = []
currently_sorting = 0
service_status = "Stopped"

def handle_sorting(max_operations, check_interval):
    global currently_sorting
    while True:
        app.logger.debug(f"Checking queue to start sorting...")
        app.logger.debug(f"\tcurrently_sorting: {currently_sorting}")
        if currently_sorting < max_operations and len(sorting_queue) > 0:
            start = time.time()
            currently_sorting += 1
            size = sorting_queue.pop()
            bubble_sort(size)
            currently_sorting -= 1
            end = time.time()
            tt = round(end - start, 3) # In seconds

            app.logger.info(f"Finished sorting array of size {size} in {tt} seconds")

            app.logger.debug(f"Waiting {check_interval} seconds to check for new sorting requests...")
        time.sleep(check_interval)

    return "Finished sorting service..."

@app.route("/start_service")
def start_service():
    global service_status
    writing_manager_thread = Thread(
            name="sorting-thread",
            target=handle_sorting,
            args=(MAX_OPERATIONS, INTERVAL, ),
            daemon=True)
    writing_manager_thread.start()
    service_status = "Started"

    return {
            'service': 'cpu_consumer',
            'status': service_status,
            'current_sorting': currently_sorting,
            'sorting_queue': len(sorting_queue)
            }


@app.route("/sort")
def sort():
    """
    Handle request for sorting.
    """
    global sorting_queue
    size = 1000
    if 'size' in request.args:
        size = int(request.args['size'])

    sorting_queue.append(size)
    msg = f"Recieved request to sort an array of size {size}"
    app.logger.info(msg)

    return { 'status': 0, 'msg': msg }

@app.route("/")
def home():
    global service_status, currently_sorting
    return { 'service': 'cpu_consumer',
            'status': service_status,
            'current_sorting': currently_sorting,
            'sorting_queue': len(sorting_queue)
            }

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", "9010"))
    app.run(debug=True, host="0.0.0.0", port=PORT)
