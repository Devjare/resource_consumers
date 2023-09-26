import os
from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
from utils import bytesto

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./files"

@app.route("/home")
@app.route("/")
def home():
    return "<h5>NET Consumer HOME</h5>"

@app.route("/download", methods=["GET"])
def download_file():
    output = {}
    filename = request.args['filename']
    uploads = app.config['UPLOAD_FOLDER']
    full_path = f'{uploads}/{filename}'

    app.logger.info(f"Recieved download request for file '{filename}'")
    if os.path.exists(full_path):
        file_size = os.stat(full_path).st_size

        file_size, display_unit = bytesto(file_size)

        msg = f"Downloading file '{filename}' of {file_size}{display_unit}"
        app.logger.info(msg)
    else:
        msg = f"Requested file '{filename}' does not exists"
        # app.logger.warning(msg)
        output = { "status": -1, "msg": msg }
        return output

    return send_from_directory(uploads, filename)

@app.route("/upload", methods=["POST"])
def upload_file():
    output = { 
              "status": 0,
              "msg": "Successfully uploaded file"
              }

    if request.method == 'POST':
        data = dict(request.form)
        file_size = int(float(data['file_size']))

        file_size, display_unit = bytesto(file_size)

        app.logger.info(f"Uploading file of {file_size}{display_unit}")
        file = request.files['file']
        filename = file.filename

        try:
            path = f"files/{secure_filename(filename)}"
            file.save(path)
            msg = f"Successfully uploaded file of {file_size}{display_unit}"
            app.logger.info(msg)
        except Exception as ex:
            # app.logger.warning(f"Failed to upload file, due to: {str(ex)}")
            output = { "status": -1,
                      "msg": "Failed to save recieved file" }
    return output

if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    PORT = os.getenv("PORT", "9008")
    app.run(debug=True, host="0.0.0.0", port=PORT)
