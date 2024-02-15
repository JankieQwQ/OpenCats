import _thread
import flask
import sys
import os

PORT = 2148
app = flask.Flask(__name__)

def commandLine():
    print('OpenCats V2 - run on {}'.format(sys.version))
    print('')
    while True:
        x = input('>')
        os.system(x)

def run():
    app.run(host='0.0.0.0',port=PORT)

@app.route('/')
def index():
    return {"code":200,"version":"OpenCats V2"}

@app.route('/opencat')
def start():
    _thread.start_new_thread(commandLine, ())

