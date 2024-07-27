from webapp import app
@app.route("/")
def indice():
    return "Flask fuciona"

@app.route("/adios")
def adios():
    return "Pues adios"

@app.route("/peliculas")
def pelis():
    return "Aqui iran las pelis"
