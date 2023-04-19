from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    valor = str(request.form.get('valor'))
    valor_quest = str(randint(1,5))
    print(type(valor))
    if request.method =="GET":
        return render_template('home.html')
    else:
        if valor == valor_quest:
            return 'Você ganhou'
        else:
            return 'você perdeu' 



@app.route('/<string:nome>')
def error(nome):
    return '<h1>Essa página não existe</h1>'

if __name__ == '__main__':
    app.run(debug=True)

