from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def page_select():
    pages = ['home', 'test', 'about']
    return render_template('home.html', pages=pages)


if __name__ == "__main__":
    app.run(debug=False, port=5000)
