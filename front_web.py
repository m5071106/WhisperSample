from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from werkzeug.utils import secure_filename
import os
import urllib.request

import sound_trans

app = Flask(__name__)

UPLOAD_FOLDER = './source'
# extensions.txtから拡張子を取得
with open('extensions.txt', 'r') as file:
    extensions = file.read()
    extensions = extensions.split('\n')
    ALLOWED_EXTENSIONS = set(extensions)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # ファイルがない場合
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            print('No selected file')
            return redirect(request.url)

        # ファイルがある場合
        if file and allowed_file(file.filename):
            print('File name: ' + file.filename)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # 変換処理
            sound_trans.sound_transcription()

            # 変換後のWebページを表示
            with open('front_web_after.html', 'r') as file:
                front_web_after_content = file.read()
            return front_web_after_content

    # 初期Webページを表示
    with open('front_web.html', 'r') as file:
        front_web_content = file.read()
    return front_web_content

if __name__ == '__main__':
    app.run()
