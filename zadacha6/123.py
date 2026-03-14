from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title='Миссия Колонизация Марса'):
    return render_template('base.html', title=title)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    context = {
        'title': 'Анкета',
        'surname': 'Иванов',
        'name': 'Иван',
        'education': 'высшее',
        'profession': 'инженер-исследователь',
        'sex': 'мужской',
        'motivation': 'Всегда мечтал побывать на Марсе!',
        'ready': 'Да'
    }
    return render_template('auto_answer.html', **context)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000')
