from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def hello_world():
#    return "<p>Hello, World!</p>"
     return render_template('home.html')

@app.route('/inspect')
def products():
    return 'This is self inspection page'

if __name__ =="__main__":
    app.run(debug=True, port= 5500)

# error handling: 1 (solved)
# flask 'No module' error appeared, so used the following command to upgrade pip to solve:
# python -m pip install --upgrade pip
# source (https://stackoverflow.com/questions/37220055/pip-fatal-error-in-launcher-unable-to-create-process-using)

# error handling: 2 (solved)
# image on  HTML was not showing in browser, had to install liver server on VSC

# error handling: 3 (solved)
# Images were not displayed + only files were showing (html, css taken into the same folder) 
 
# error handling: 4 (solved)
# live server was not working (app.py was configuared and verified port)
 
# error handling: 5 (solved)
# H1 heading and paragraph were not aligned across
# Solved by removing hero-section parent func 
# https://www.youtube.com/watch?v=s3GTej92hvU&list=PL0-e1OMq5RP4BIrTQPrqu6Jxsfp94xK8Z&index=7

# error handling: 6 (solved)
# template not found, listing directory
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files
# https://jinja.palletsprojects.com/en/2.11.x/
# html, css and js all in a same folder, either template or static; and run on Live Server

# error handling: 7 (unsolved)
# only html shows up while running through cmd

