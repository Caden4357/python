from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/some_route')
def some_function_name():
    return render_template("sucess.html")

app.run(debug=True)