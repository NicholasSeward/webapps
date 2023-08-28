# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
    
@app.route('/bio')
def bio():
    return send_from_directory(directory=app.static_folder, path='bio.html')

@app.route('/links')
def links():
    return send_from_directory(directory=app.static_folder, path='links.html')

@app.route('/schedule')
def schedule():
    return send_from_directory(directory=app.static_folder, path='schedule.html')

if __name__=="__main__":
	app.run(host='0.0.0.0', port=80)
