import mysql.connector
from flask import Flask, jsonify, request
# from banco import *

host = "sergio-1.chvt2nz4puya.us-east-1.rds.amazonaws.com"
usuario = "admin"
senha = 'xande1972'
porta = 3306
banco = 'chinook'

app = Flask(__name__)


@app.route("/")

def padrao():
    return "<H1>SD é Fácil e  Brabo </H1>"

@app.route("/nome/<nome>")

def imprime_nome(nome):
    return f"<H1>Olá {nome}</H1>"
    
@app.route("/sobrenome")

def imprime_nome_sobrenome():
    return f"<H1>Olá {request.args['nome']} {request.args['sobrenome']} </H1>"    


app.config['JSON_AS_ASCII'] = False
app.run(host='0.0.0.0', port= '8080', debug=True)