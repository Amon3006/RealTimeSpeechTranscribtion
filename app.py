from flask import Flask, render_template, jsonify
import os
# os.system('python engine.py')
from subprocess import run
app = Flask(__name__)

@app.route('/')
def index():
   
   return render_template('demo.html')
   
@app.route("/start_asr")
def start():
    run('python engine.py',shell=True)
    return jsonify("speechrecognition start success!")


@app.route("/get_audio")
def get_audio():
    f = open('transcribe.txt','r')
    text = f.read() 
    return jsonify(text)

if __name__ == "__main__":
        app.run(debug = True, port = 3000)
    