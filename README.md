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

## 09_Jinja2
templating modern dan user friendly untuk python
1. http://127.0.0.1:5000/
2. http://127.0.0.1:5000/looping_hari
3. http://127.0.0.1:5000/about
4. http://127.0.0.1:5000/contact

## 10_ParsingParamsViaURLEndpoint
Parsing parameters or value with URL endpoint
1. Value Parsing
   - 127.0.0.1:5000/<int:value>
   - 127.0.0.1:5000/<string:words>
   - 127.0.0.1:5000/<float:floatValue>
   - 127.0.0.1:5000/<bebas>
2. Argument Parser
   - from flask import request
   - 127.0.0.1:5000?nilai=100
3. Test
   - 127.0.0.1:5000/parsingInteger/99
   - 127.0.0.1:5000/parsingFloat/8.83
   - 127.0.0.1:5000/parsingString/ultraman
   - 127.0.0.1:5000/argumentParsing?sayaAdalah=batman
4. 
