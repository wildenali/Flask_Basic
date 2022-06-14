from flask import Flask, render_template # render_template untuk pisahin html file dari sini, atau ambil template html di folder templates
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hello_name/<user>')
def helo_name(user):
    return render_template('helo_name.html', namanya = user)

@app.route('/helo_nilaii/<int:nilai>')
def helo_nilai(nilai):
    return render_template('hello_nilai.html', berapanilainya = nilai)

@app.route('/result')
def result():
    dict = {'phy':50,'che':60,'maths':70}
    return render_template('result.html', hasil = dict)


if __name__ == '__main__':
    app.run(debug = True)