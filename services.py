
from pprint import pprint
from app import dummy_every_composicoes
composicoes = dummy_every_composicoes()
# Usar DB Browser (SQLite)


def get_composicoes():
    return composicoes


def get_composicoes_by_codigo(codigo):
    return [item for item in composicoes if item.get('codigo', '') == codigo]


def cria_composicao(composicao):
    pass


def altera_composicao(codigo, composicao):
    pass


def remover_composicao(codigo):
    return True
    # composicoes[indice].update(composicao)
# pprint(get_composicoes_by_codigo(104658))
