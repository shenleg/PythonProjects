import os.path

from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/upload"
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024


@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    else:
        f = request.files["file"]
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], f.filename))
        return render_template("upload.html")


@app.route('/download')
def download():
    return send_from_directory(app.config["UPLOAD_FOLDER"], "图片.png", as_attachment=True)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
