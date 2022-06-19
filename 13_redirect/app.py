from flask import Flask, render_template, request
from flask import session   # import session
from flask import url_for, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "inisecretkey"   # nilainya bebas terserah

@app.route("/")
def my_index():
    return render_template("index.html")

@app.route("/about")
def my_about():
    return render_template("about.html")

@app.route("/contact")
def my_contact():
    return render_template("contact.html")

@app.route("/my_index_redirect")
def my_index_redirect():
    return redirect(url_for('my_index'))

@app.route("/my_about_redirect")
def my_about_redirect():
    return redirect(url_for('my_about'))

@app.route("/my_contact_redirect")
def my_contact_redirect():
    return redirect(url_for('my_contact'))

if __name__ == "__main__":
    app.run(debug=True, port=5001)