from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=['GET'])
def page_select():
    pages = ['home', 'try it yourself', 'about']
    return render_template('home.html', pages=pages)


@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')

@app.route("/try-it-yourself", methods=['GET'])
def try_it_yourself():
    return render_template('try_it.html')

@app.route("/contact-us", methods=['GET'])
def contact_us():
    return render_template('contact_us.html')

@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html') #make html template

@app.route("/sign-up", methods=['GET'])
def sign_up():
    return render_template('sign_up.html')#make html template

if __name__ == "__main__":
    app.run(debug=False, port=5000)


#about, test it your self, meny