from flask import Flask, url_for, render_template, redirect
from answer import AnswerForm
import os

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config['SECRET_KEY'] = 'ivcbxjhkegr213898cbvxjk324jkhbcvx832'


@app.route('/')
def index():
    return redirect('/answer')


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    form = AnswerForm()
    if form.validate_on_submit():
        data = {
            'email': form.email.data
        }
        print(data)
    return render_template('answer.html', form=form)


if __name__ == '__main__':
    app.run(host='localhost', port=80)
