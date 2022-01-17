from flask import Flask, render_template, request
from flask import request

app = Flask(__name__)


@app.route('/', method=['GET', 'POST'])
def hello():
    return render_template('hello.html')


@app.route('/hello_name', method=['POST'])
def hello_name():
    name = request.form.get('name')
    return render_template('hello_name.html', name=name)


if __name__ == '__main__':
    app.run()
