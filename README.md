# Install Flask

Install Virtual Environment
`$ pip install virtualenv`

Create Virtual Environment
`$ virtualenv venv`

Activate environment
- Linux `$ venv/bin/activate`
- Windows `$ venv\scripts\activate`

`$ pip install Flask`

Run Flask app
python -m flask run

The development server looks for app.py by default.

if no app.py, how to change
set FLASK_APP=hello.py

## 01_HelloWorld

1. Change directory to the project
   ```cmd
   $ cd 01_HelloWorld
   ```
2. How to run the server app
   ```cmd
   $ python -m flask run
   ```
   or
   ```cmd
   $ python app.py
   ```
3. Open http://127.0.0.1:5000
<br>


## 02_HTTPMethods
1. Change directory to the project
   ```cmd
   $ cd 02_HTTPMethods
   ```
2. Change the the environment variable Flask server app
   ```terminal
   $ export FLASK_APP=A_post_method.py  // use this if using linux
   ```
   ```cmd
   $ set FLASK_APP=A_post_method.py     // use this if using windows
   ```
3. Run the server app
   ```sh
   $ python -m flask run
   ```
   or
   ```cmd
   $ python A_post_method.py
   ```
<br>

## 03_Templates
### 03_A_templating
1. Change directory to the project
   ```cmd
   $ cd 03_Templates/03_A_templating
   ```
2. Run the server app
   ```sh
   $ python -m flask run
   ```
   or
   ```cmd
   $ python app.py
   ```
3. Open app
   - http://127.0.0.1:5000/index
