from flask import Flask, render_template, request
from flask import session   # import session

app = Flask(__name__)
app.config["SECRET_KEY"] = "inisecretkey"   # nilainya bebas terserah

@app.route("/")
def indeks():
    nilai = 99
    return render_template("index.html", kirimNilai=nilai)

@app.route("/looping_hari")
def looping_hari():
    hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
    cuaca = "hujan"
    return render_template("index_hari.html", kirimHari=hari, kirimCuaca=cuaca)

@app.route("/about")
def aboutku():
    return render_template("about.html")

# Parsing integer value
@app.route("/parsingInteger/<int:nilaiku>")
def parsingIntegerku(nilaiku):
    return "nilainya adalah: {}".format(nilaiku)

# Parsing integer value
@app.route("/parsingFloat/<float:nilaiFloat>")
def parsingFloatku(nilaiFloat):
    return "nilainya adalah: {}".format(nilaiFloat)

# Parsing string
@app.route("/parsingString/<string:stringku>")
def parsingStringku(stringku):
    return "saya adalah {}".format(stringku)

# Argument parser
@app.route("/argumentParsing")
def argumentParsingku():
    data = request.args.get("sayaAdalah")
    return "nilai saya adalah {}".format(data)

@app.route("/contact")
def contactku():
    return render_template("contact.html")

@app.route("/halaman/<int:nilaiSession>")
def session_1(nilaiSession):
    session["nilaiku"] = nilaiSession   # nama session bebas
    return "Berhasil set nilai session"

@app.route("/halaman/lihat")
def view_session_1():
    data = session["nilaiku"]
    return "Nilai yang telah di set adalah {}".format(data)

if __name__ == "__main__":
    app.run(debug=True)