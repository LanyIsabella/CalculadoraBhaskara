from flask import Flask, render_template, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def calcular():
    a = None
    b = None
    c = None
    delta = None
    x1 = None
    x2 = None
    erro = None
    
    try:
        a = float(request.form.get('a'))
        if a == 0.00:
            raise ValueError
        b = float(request.form.get('b'))
        c = float(request.form.get('c'))
        
        delta = (b**2) - (4*a*c)
        if delta < 0:
            erro = "O valor de delta é menor que 0, portanto, não existe raiz real para essa equação."
        else:
            x1 = (-b + sqrt(delta)) / (2 * a)
            x2 = (-b - sqrt(delta)) / (2 * a)
    except ValueError:
        erro = "Valor inválido"
    return render_template('index.html', erro=erro, x1=x1, x2=x2, delta=delta)
        