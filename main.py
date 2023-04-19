from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    valor = request.form.get('valor')

    return render_template('home.html')
    randint(1,5)
    

    # numero = 0
    # if valorRecebido ==numero:
        # return 'Você ganhou'



@app.route('/<string:nome>')
def error(nome):
    return '<h1>Essa página não existe</h1>'

if __name__ == '__main__':
    app.run(debug=True)

