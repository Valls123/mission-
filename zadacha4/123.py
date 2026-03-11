from flask import Flask, render_template
import json

app = Flask(__name__)

professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инжер по терраформированию',
               'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
               'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман',
               'пилот дронов']


@app.route('/')
@app.route('/index')
def index():
    return render_template('odd_even.html', number=2)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=3)


@app.route('/list_prof/<style>')
def list_prof(style):
    return render_template('list_prof.html', style=style, prof_list=professions)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
