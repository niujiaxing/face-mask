from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
import os
import base64
from tensorflow_infer_niu import main
from utils.distinguish_fish import get_fish



app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'mp4'])
IMAGE = set(['png', 'jpg', 'JPG', 'PNG'])
VIDEO = set(['mp4'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def allowed_img_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in IMAGE


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/fish")
def fish():
    return render_template("fish.html")


# 上传图片
@app.route('/up_photo', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['photo']
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.', 1)[1]
        fname = "img\\img." + ext
        f.save(fname)
        if ext in IMAGE:
            main(1, fname, 0)  # ['p1.py']
        else:
            main(0, 0, fname)
        return render_template("upload.html")
    else:
        return render_template("upload.html", msg="上传失败,请检查数据格式是否正确！")


@app.route('/camera')
def camera():
    main(0, 0, 0)
    return render_template("upload.html")


@app.route('/up_fish', methods=['POST'])
def distinguish_fish():

    f = request.files['photo']
    if f and allowed_img_file(f.filename):
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.', 1)[1]
        fname = "img\\fish." + ext
        f.save(fname)
        fish = get_fish(fname)
        return render_template("fish.html", fishname=fish)
    else:
        return render_template("fish.html", msg="上传失败,请检查数据格式是否正确！")





if __name__ == '__main__':
        app.run()