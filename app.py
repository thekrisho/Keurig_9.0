# Import library
import threading
import subprocess
import os
import sys
from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

# Define Script / Subprocess
def run_script():
    theproc = subprocess.Popen([sys.executable, "brew.py"])
    theproc.communicate()

# Home
@app.route('/')
def index():
    return render_template('home.html')
    return 'Enter /brew to begin'

# Val
@app.route('/val')
def val():
    return render_template('val.html')

# Brew
@app.route('/brew')
def brew():
    threading.Thread(target=lambda: run_script()).start()
    return render_template('load.html')

# Clean
@app.route('/clean')
def clean():
	return render_template('home.html')

# Reset
@app.route('/reset')
def reset():
	return render_template('home.html')

# End
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
   #app.run(port=4004, debug=True, host'127.0.0.1')
