from flask import Flask
from flask import request
from flask import render_template

import pgen


app = Flask(__name__)
app.jinja_env.cache = {}
app.jinja_env.line_statement_prefix = '%'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/show", methods=['POST'])
def show_pass():
    return render_template('result.html', password=get_pass())


@app.route("/get", methods=['POST'])
def get_pass():
    return pgen.gen_pass(
        login=request.form['login'],
        password=request.form['password'],
        site=request.form['site'],
        secret_key=app.secret_key,
        length=int(request.form['length']),
    )


@app.errorhandler(404)
def page_not_found(error):
    return 'Page not found!'
