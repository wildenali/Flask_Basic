from flask import Flask

app = Flask(__name__)

@app.route("/index")
def indexku():
    return "<h1>Hallo Flask templating</h1>"

if __name__ == "__main__":
    app.run(debug=True)