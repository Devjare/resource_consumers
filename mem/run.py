import random
import os
import psutil
import time
from flask import Flask, request
from utils import bytesto

app = Flask(__name__)

DEFAULT_THRESHOLD = str(psutil.virtual_memory().total / 2)
THRESHOLD = int(float(os.getenv("THRESHOLD", DEFAULT_THRESHOLD)))
MEM_UTILIZATION = 0
CONSUMER = '' * int(MEM_UTILIZATION)

def append(mem):
    global CONSUMER, MEM_UTILIZATION
    past_consumption = len(CONSUMER)
    CONSUMER += ('*' * mem)
    MEM_UTILIZATION += mem

def substract(mem):
    global CONSUMER, MEM_UTILIZATION
    CONSUMER = CONSUMER[0:len(CONSUMER) - mem]
    MEM_UTILIZATION -= mem if MEM_UTILIZATION > 0 and MEM_UTILIZATION >= mem else 0

@app.route("/add")
def add_memory():
    global CONSUMER, MEM_UTILIZATION
    mem = request.args["mem"]
    formatted_mem = 0
    mem = int(mem)
    formatted_mem, unit = bytesto(mem)
    try:
        app.logger.info(f"Appending {formatted_mem}{unit} to current consumer.")

        if MEM_UTILIZATION + mem > THRESHOLD:
            msg = f"Cannot append more memory threshold achieved. Free some first."
            app.logger.warning(msg)
            return { "status": -1, "msg": msg }
        else:
            append(mem)
            _value, _unit = bytesto(MEM_UTILIZATION)
            msg = f"Successfully appended to consumer. Current consumption {_value}{_unit}"
            app.logger.info(msg)
    except Exception as ex:
        app.logger.error(f"Failed to append more memory due to: {ex}")

    return {
            "status": 0,
            "msg": f"Successfully appended {formatted_mem}{unit}."
            }


@app.route("/reduce")
def reduce_memory():
    # 1 GB = 1024 * 1024 * 1024 * 1
    global CONSUMER, MEM_UTILIZATION
    mem = request.args["mem"]
    unit = 0
    mem = int(mem)
    f_mem = bytesto(mem)
    try:
        msg = f"Substracting {f_mem[0]}{f_mem[1]} from current consumer."
        app.logger.info(msg)

        if MEM_UTILIZATION == 0:
            msg = f"Cannot substract memory consumption already is 0."
            app.logger.warning(msg)
            return { "status": -1, "msg": msg }
        elif mem >= MEM_UTILIZATION:
            substract(MEM_UTILIZATION)
            c_f_mem = bytesto(MEM_UTILIZATION) # current_formatted_mem
            f"Successfully substracted from consumer. Current consumption {c_f_mem[0]}{c_f_mem[1]} from current consumer"
            app.logger.info(msg)
        else:
            substract(mem)
            c_f_mem = bytesto(MEM_UTILIZATION) # current_formatted_mem
            f"Successfully substracted from consumer. Current consumption {c_f_mem[0]}{c_f_mem[1]} from current consumer"
            app.logger.info(msg)

    except Exception as ex:
        app.logger.error(f"Failed to substract more memory due to: {ex}")

    return { 
            "status": 0, 
            "msg": f"Successfully substracted {f_mem[0]}{f_mem[1]}."
            }

@app.route("/")
@app.route("/home")
def home():
    return "<h5>Memory consumer HOME</h5>"

@app.route("/help")
def show_help():
    """
        Return possible actions, defined by @app.route declarations
    """
    app.logger.info("Showing help")
    return { 
            "functions": { 
                "/add": { 
                    "req_type": "GET", "args": {"mem": { "type": "Integer" } },
                    "description": "Increase the memory consumption object size by the specified `mem` bytes"
                },
                "/reduce": {
                    "req_type": "GET", "args": { "mem": { "type": "Integer" } },
                    "description": "Reduce the memory consumption object size by the specified `mem` bytes"
                }
            }
        }


if __name__ == "__main__":
    PORT = int(os.getenv("PORT", "9009"))
    app.run(debug=True, host="0.0.0.0", port=PORT)
