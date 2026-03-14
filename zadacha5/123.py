import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/img'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 МБ

# Разрешённые расширения
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    filename = None
    if request.method == 'POST':
        # Проверяем, есть ли файл в запросе
        if 'photo' not in request.files:
            return redirect(request.url)
        file = request.files['photo']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # Сохраняем с фиксированным именем (перезаписываем)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded.jpg'))
            return redirect(url_for('index'))
    # Проверяем, существует ли уже загруженное фото
    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded.jpg')):
        filename = 'uploaded.jpg'
    return render_template('index.html', filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
