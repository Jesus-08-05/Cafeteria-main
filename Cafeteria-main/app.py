from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.Config')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quienes')
def quienes():
    return render_template('quienes.html')


@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/Seccion')
def Seccion():
    return render_template('Seccion.html')

if __name__ == '__main__':
    app.run(debug=True)
