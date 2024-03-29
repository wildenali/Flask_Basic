from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/contact")
def contactku():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)