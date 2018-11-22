from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/nodo1")
def nodo1():
    return render_template("nodo1.html")
@app.route("/nodo2")
def nodo2():
    return render_template("nodo2.html")
@app.route("/lineas")
def lineas():
    return render_template("lineas.html")
if __name__ == '__main__':
    app.run(debug=True,port=3000)