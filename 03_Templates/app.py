from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def helo_name(user):
    return render_template('hello.html', namanya = user)

@app.route('/nilai/<int:nilai>')
def helo_nilai(nilai):
    return render_template('hello.html', berapanilainya = nilai)

@app.route('/result')
def result():
    dict = {'phy':50,'che':60,'maths':70}
    return render_template('hello.html', hasil = dict)


if __name__ == '__main__':
    app.run(debug = True)