from main import app
from extensions import db
import json
import requests
from services import cria_composicoes


def init_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()


def fill_banco():
    # Lê os dados
    with open('./base/composicoes.json', 'r', encoding='utf-8') as arquivo_json:
        # Carrega o conteúdo do arquivo JSON para um objeto Python (neste caso, uma lista de dicionários)
        dados = json.load(arquivo_json)

    with app.app_context():
        db.drop_all()
        db.create_all()
        cria_composicoes(dados)


if __name__ == 'main':
    init_banco()
