from flask import request
from flask import render_template

from . import app
from . import utils


@app.route("/")
def form():
    return render_template('form.html')


@app.route("/result", methods=['POST'])
def result():
    return render_template('result.html', password=get())


@app.route("/get", methods=['POST'])
def get():
    user_data = {
        'login': request.form['login'],
        'password': request.form['password'],
        'site': request.form['site'],
        'length': int(request.form['length']),
    }

    if not request.form.get('ignore'):
        user_data['secret_key'] = app.secret_key

    return utils.gen_pass(**user_data)


@app.errorhandler(404)
def page_not_found(error):
    return 'Page not found!'
