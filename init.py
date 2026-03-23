# from main import app
# from extensions import db
import json
import requests
from services import cria_composicoes, cria_subcomposicoes


def init_banco(app, db):
    with app.app_context():
        db.drop_all()
        db.create_all()


def fill_banco(app, db):
    # Lê os dados
    with open('./base/composicoes.json', 'r', encoding='utf-8') as arquivo_json:
        # Carrega o conteúdo do arquivo JSON para um objeto Python (neste caso, uma lista de dicionários)
        dados = json.load(arquivo_json)

    # Lê os dados
    with open('./base/subcomposicoes.json', 'r', encoding='utf-8') as arquivo_sub_json:
        # Carrega o conteúdo do arquivo JSON para um objeto Python (neste caso, uma lista de dicionários)
        dados_sub = json.load(arquivo_sub_json)
        # print(dados_sub)

    with app.app_context():
        db.drop_all()
        db.create_all()
        cria_composicoes(dados)
        # cria_subcomposicoes(dados_sub)


if __name__ == 'main':
    # init_banco()
    # fill_banco()
    print('Concluido')
