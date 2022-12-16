import random
import psutil
import os
import time
from flask import Flask, request

app = Flask(__name__)

TOTAL_MEM = psutil.virtual_memory().total

lowest = 0
low = 0.3
mid = 0.6
high = 0.9

x = 0

LOW = (lowest, low)
MED = (low, mid)
HIGH = (mid, high)

s = ''

def reset_variables():
    os.environ["UTILIZATION"] = "1"
    os.environ["STOP_CONSUMPTION"] = "0"

def set_consumption(level):
    if level == 1:
        consumption_percentage = random.uniform(LOW[0], LOW[1])
        mem_utilization = consumption_percentage * TOTAL_MEM
        s = ' ' * int(mem_utilization)
        print(f"MEM_CONSUMER LOW, consuming {mem_utilization} bytes of RAM")
    elif level == 2:
        consumption_percentage = random.uniform(MED[0], MED[1])
        mem_utilization = consumption_percentage * TOTAL_MEM
        s = ' ' * int(mem_utilization)
        print(f"MEM_CONSUMER MED, consuming {mem_utilization} bytes of RAM")
    elif level == 3:
        consumption_percentage = random.uniform(HIGH[0], HIGH[1])
        mem_utilization = consumption_percentage * TOTAL_MEM
        s = ' ' * int(mem_utilization)
        print(f"MEM_CONSUMER HIGH, consuming {mem_utilization} bytes of RAM")

@app.route("/change_utilization", methods=["GET"])
def change_utilization():
    new_utilization = request.args.get("utilization_level")
    print(f"New utilization = {new_utilization}, type={type(new_utilization)}")
    os.environ["UTILIZATION"] = new_utilization
    return { "status": "Success", 
            "message": "Utilization level succesfully changed." }

@app.route("/stop_consumption", methods=["GET"])
def stop_consuming():
    print(f"Stopping consumption...")
    os.environ["STOP_CONSUMPTION"] = "1"
    return "Stopping consumption..."

@app.route("/start_consumption", methods=["GET"])
def start_consuming():
    start_time = time.monotonic()
    stop_consumption = int(os.getenv("STOP_CONSUMPTION","0"))
    while not stop_consumption:
        current_time = time.monotonic()
        elapsed = current_time - start_time

        if  int(elapsed) % 5 == 0:
            UTILIZATION = int(os.getenv("UTILIZATION", "1"))
            set_consumption(UTILIZATION)

            time.sleep(1)

            stop_consumption = int(os.getenv("STOP_CONSUMPTION","0"))
    
    reset_variables()
    return "Consumption stopped..."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=90997)
