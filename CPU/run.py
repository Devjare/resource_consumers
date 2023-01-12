from flask import Flask, request
import subprocess
import os
import signal

app = Flask(__name__)

global current_level
process_list = []
LOW_SIZE = 100
MED_SIZE = 10000
HIGH_SIZE = 1000000

@app.route("/start_consumption", methods=["GET"])
def start_consumption():
    global current_level
    try:
        level = int(request.args.get("utilization_level"))
    except Exception as ex:
        print(f"Failed to parse argument: utilization_level. Error: {ex}")
        level = None

    if level == None:
        level = 1
    
    current_level = level

    # Lvl1 = 3, lvl2 = 6, lvl3 = 8
    if level == 1:
        lvl_range = 3
        n = LOW_SIZE
    if level == 2:
        lvl_range = 6
        n = MED_SIZE
    if level == 3:
        lvl_range = 8
        n = HIGH_SIZE

    for i in range(lvl_range):
        start_new_process(n)

    return { "pids": process_list }

@app.route("/stop_consumption", methods=["GET"])
def stop_consumption():
    for i in range(len(process_list)):
        kill_process(process_list[i])

    return { "pids": process_list }

@app.route("/current_processes")
def get_current_processes():
    return { 'current_processes': str(process_list) }

def start_new_process(n=10000):
    process = subprocess.Popen(args=["python", "cpu_consumer.py", f"{n}"])
    process_list.append(process.pid)

@app.route("/change_utilization")
def change_utilization():
    global current_level
    # STOP PREVIOUS PROCESSES
    try:
        new_level = int(request.args.get("utilization_level"))
    except Exception as ex:
        print(f"Failed to parse argument: utilization_level. Error: {ex}")
        new_level = None

    if new_level == None:
        new_level = 1

    # Lvl1 = 3, lvl2 = 6, lvl3 = 8
    if new_level == 1:
        lvl_range = 3
        n = LOW_SIZE
    if new_level == 2:
        lvl_range = 6
        n = MED_SIZE
    if new_level == 3:
        lvl_range = 8
        n = HIGH_SIZE
    
    if new_level > current_level:
        for i in range(lvl_range - len(process_list)):
            start_new_process(n)
    elif new_level < current_level:
        # KILL len(process_list) - lvl_range
        print(f"range {len(process_list) - lvl_range}")
        for i in range(len(process_list) - lvl_range):
            print(f"Killing process: {i}={process_list[i]}")
            os.kill(process_list[i], signal.SIGTERM)
            process_list.pop(i)
    
    current_level = new_level
    return { 'processes': str(process_list) }
def kill_process(pid):
    os.kill(pid, signal.SIGTERM)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8567)
