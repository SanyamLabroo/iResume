from flask import Flask, app,render_template

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/inner-page")

def inner_page():
    return render_template('inner-page.html')


if __name__ == "__main__":
    app.run(debug=True)