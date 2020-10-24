from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home/index.html", username="Test")


@app.route('/front-end')
def front_end():
    # return render_template("home/index.html", username="Test")
    return {'success': 'Service is running'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
