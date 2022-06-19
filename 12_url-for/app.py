from flask import Flask, render_template, request
from flask import session   # import session

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

if __name__ == "__main__":
    app.run(debug=True, port=5001)