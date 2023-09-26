import os
from flask import Flask, request
from utils import bytesto, sizes

app = Flask(__name__)

FILE_NAME="testfile.txt"
THRESHOLD = int(os.getenv("THRESHOLD", str(sizes['GB'] * 30)))
CURRENT_SIZE = 0

def append_to_file(size=None):
    """
        append 'size' in bytes to file.
    """
    # if exists file write_mode = append, else write
    write_mode = "a" if os.path.isfile(FILE_NAME) else "w"
    msg = "Successfully written new data!"
    status = 0 # 0 Errors
    try:
        with open(FILE_NAME, write_mode, encoding="utf-8") as file:
            file.write('0' * size)
    except Exception as ex:
        msg = f"Failed to write to file due to: {str(ex)}"
        status = -1 # Failed

    return {
            "status": status,
            "msg": msg
            }

@app.route("/append", methods=["GET"])
def append():
    global CURRENT_SIZE
    size = None
    output = { }
    try:
        size = int(request.args['size'])
        _value, _unit = bytesto(int(size))
    
        if CURRENT_SIZE + size > THRESHOLD:
            _value, _unit = bytesto(CURRENT_SIZE)
            app.logger.info(f"Threshold achieved and cannot append more. Current size: {_value}{_unit}.")
            msg = f"Failed to append to file due to THRESHOLD ACHIEVED."
            output = { 'status': -1, 'msg': msg }
            return output

        app.logger.info(f"Trying to append {_value}{_unit} to file.")

        output = append_to_file(int(size))

        # appended = f"{_value}{_unit}"
        CURRENT_SIZE = int(os.path.getsize(FILE_NAME))
        _value, _unit = bytesto(CURRENT_SIZE)
        current = f"{_value}{_unit}"
        msg = f"Successfully written to file. Current file size: {current}."
        app.logger.info(msg)

    except Exception as ex:
        print(ex)
        msg = f"Failed to append to file due to {str(ex)}"
        # app.logger.error(msg)
        output = { 'status': -1, 'msg': msg }

    return output

@app.route("/delete_file", methods=["GET"])
def delete_file():
    global CURRENT_SIZE
    output = {}
    try:
        msg = f"Recieved request to remove file."
        # app.logger.info(msg)
        status = 0
        try:
            if os.path.exists(FILE_NAME):
                os.remove(FILE_NAME)
                msg = f"Successfully deleted file."
                CURRENT_SIZE = 0
            else:
                msg = f"Could not remove file, does not exists."
        except Exception as ex:
            msg = f"Failed to delete file, doesn't exists."
            status = -2
        # app.logger.info(msg)
        output = { 'status': status, 'msg': msg }
    except Exception as ex:
        msg = f"Failed to delete file due to: {str(ex)}"
        # app.logger.warning(msg)
        output = { 'status': -2, 'msg': msg }
    return output

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return "<h5>FS Consumer home!</h5>"

if __name__ == "__main__":
    PORT = os.getenv("PORT", "9007")
    app.run(debug=True, host="0.0.0.0", port=PORT)
