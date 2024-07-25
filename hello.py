from flask import Flask

app = Flask(__name__)

@app.route('/')
def indice():
    return "Hola, mundo, estoy funcionando."

@app.route("/adios")
def elnombredefuncionquequiera():
    return "Pues adios"