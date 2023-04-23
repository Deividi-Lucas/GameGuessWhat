# Importação das bibliotecas
from flask import Flask, render_template, request
from random import randint


# Variável principal
app = Flask(__name__)


# Definição de rotas
@app.route('/', methods=['GET', 'POST'])
def home():
    valor = str(request.form.get('valor'))
    valor_quest = str(randint(1, 5))
    if request.method == "GET":
        return render_template('home.html')
    else:
        if valor == valor_quest:
            return '<h1>Você ganhou</h1>'
        else:
            return '<h1>você perdeu</h1>'


# Rota inválida
@app.route('/<string:nome>')
def error(nome):
    return '<h1>Essa página não existe</h1>'


# Run server
if __name__ == '__main__':
    app.run(debug=True)
