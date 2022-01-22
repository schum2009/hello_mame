from flask import Flask, render_template, request

app = Flask(__name__)
user_name = []


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('hello.html')


@app.route('/hello_name', methods=['POST'])
def hello_name():
    name = request.form.get('name')

    if name in user_name:
        return render_template('seen_you_before.html', name=name)


    else:
        user_name.append('name')
        return render_template('hello_name.html', name=name)


@app.route('/username', methods=['POST'])
def username():
    return render_template('username.html')


if __name__ == '__main__':
    app.run()
