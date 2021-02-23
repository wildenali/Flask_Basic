from flask import Flask, redirect, url_for

app = Flask(__name__)

# Basic ================================
@app.route('/')
def hello():
    return 'HalO Bosku'
# Basic ================================

# url ================================
@app.route('/inipage')
def hello_page():
    return 'Halo page'

@app.route('/namaorang/<nama>')
def nama_orang(nama):
    return 'Hay %s' % nama

@app.route('/noktp/<int:noKTP>')
def no_ktp(noKTP):
    return 'No KTP nya %i' % noKTP
# url ================================

# URL Building ================================
# Import redirect dan url_for dulu di atas dengan sintak from flask import redirect, url_for
@app.route('/mimin')
def hello_mimin():
   return 'Hello mimin'

@app.route('/tamu/<tamu>')
def hello_tamu(tamu):
   return 'Hello tamu %s' % tamu

@app.route('/user/<nama>')
def user_name(nama):
    if nama == 'admin':
        return redirect(url_for('hello_mimin'))
    else:
        return redirect(url_for('hello_tamu', tamu = nama))
# URL Building ================================

if __name__ == "__main__":
    app.run()