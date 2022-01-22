from flask import Flask, render_template, request

app = Flask(__name__)
user_names = []


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('hello.html')


@app.route('/hello_name', methods=['POST'])
def hello_name():
    name = request.form.get('name')

    if name in user_names:
        return render_template('seen_you_before.html', name=name)

    else:
        user_names.append(name)
        return render_template('hello_name.html', name=name)


@app.route('/usernames', methods=['POST'])
def usernames():
    return render_template('usernames.html', my_list=user_names)


if __name__ == '__main__':
    app.run()
