from flask import (Flask, render_template, request, make_response, 
                    session, url_for, redirect, flash)
app = Flask(__name__)
app.secret_key = 'randomstringapapun'

@app.route('/')
def index():
    search = request.args.get('search')
    return render_template('index.html', search=search)

@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def show_login():
    if request.method == 'POST':
        # res = make_response('Email kamu adalah ' + request.form['email'])
        # res.set_cookie('email_user', request.form['email'])
        session['username'] = request.form['email']
        flash('kamu berhasil login', 'success')
        return redirect(url_for('show_profile', username=session['username']))
    
    if 'username' in session:
        username = session['username']
        return redirect(url_for('show_profile', username=username))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('show_login'))

@app.route('/getcookie')
def get_cookie():
    email = request.cookies.get('email_user')
    return 'Email yang tersimpan di cookie adalah ' + email

if __name__ == "__main__":
    app.run(debug=True)