
from flask import request
from extensions import db
from models import Composicao, Subcomposicao

# Usar DB Browser (SQLite)


def get_composicoes():
    '''
    Retorna uma lista com todas as composições no banco de dados
    '''
    composicoes = Composicao.query.all()
    lista_composicoes = []
    for composicao in composicoes:
        nova_composicao = {}
        nova_composicao['codigo'] = composicao.codigo
        nova_composicao['descricao'] = composicao.descricao
        nova_composicao['grupo'] = composicao.grupo
        nova_composicao['custo_unitario'] = composicao.custo_unitario
        nova_composicao['unidade'] = composicao.unidade
        lista_composicoes.append(nova_composicao)

    return composicoes


def get_composicoes_by_codigo(codigo):
    '''
    Retorna a composição com o código fornecido.
    Caso não encontrada lança uma exceção.
    '''
    composicao = Composicao.query.filter_by(codigo=codigo).first()
    if not composicao:
        return None

    nova_composicao = {}
    nova_composicao['codigo'] = composicao.codigo
    nova_composicao['descricao'] = composicao.descricao
    nova_composicao['grupo'] = composicao.grupo
    nova_composicao['custo_unitario'] = composicao.custo_unitario
    nova_composicao['unidade'] = composicao.unidade

    return nova_composicao


def get_subcomposicoes(codigo):
    '''
    Retorna a composição com o código fornecido.
    Caso não encontrada lança uma exceção.
    '''
    composicoes = Subcomposicao.query.filter_by(id_composicao=codigo)
    if not composicoes:
        return None

    subcomposicoes = []
    for subcomposicao in subcomposicoes:
        nova_subcomposicao = get_composicoes_by_codigo(subcomposicao.codigo)
        # Atualiza o coeficiente da subcomposicao
        nova_subcomposicao['coeficiente'] = subcomposicao.coeficiente
        subcomposicoes.append()

    return nova_subcomposicao


def cria_composicao(composicao):
    '''
    Adiciona uma única composição ao banco de dados.
    Caso ela já exista no banco de dados ou esteja com informações faltantes, lança uma exceção.
    '''

    nova_composicao = request.get_json()
    composicao = Composicao(
        codigo=nova_composicao['codigo'],
        descricao=nova_composicao['descricao'],
        grupo=nova_composicao['grupo'],
        custo_unitario=nova_composicao['custo_unitario'],
        unidade=nova_composicao['unidade']
    )
    db.session.add(composicao)
    db.session.commit()


def cria_composicoes(composicoes):
    '''
    Adiciona uma lista de composições ao banco de dados.
    São adicionadas apenas as composições válidas.
    '''
    # composicoes = request.get_json()['composicoes']
    for nova_composicao in composicoes:
        try:
            composicao = Composicao(
                codigo=nova_composicao['codigo'],
                descricao=nova_composicao['descricao'],
                grupo=nova_composicao['grupo'],
                custo_unitario=nova_composicao['custo_unitario'],
                unidade=nova_composicao['unidade']
            )
            db.session.add(composicao)
        except Exception as e:
            print(e)
    db.session.commit()


def cria_subcomposicoes(subcomposicoes):
    '''
    Adiciona uma lista de composições ao banco de dados.
    São adicionadas apenas as composições válidas.
    '''
   # composicoes = request.get_json()['composicoes']
    for nova_subcomposicao in subcomposicoes:
        try:
            subcomposicao = Subcomposicao(
                codigo=nova_subcomposicao['codigo'],
                id_composicao=nova_subcomposicao['id_composicao'],
                coeficiente=nova_subcomposicao['coeficiente']
            )
            db.session.add(subcomposicao)
        except Exception as e:
            print(e)
    db.session.commit()


def altera_composicao(codigo, composicao):
    '''
    Altera as informações de uma única composição com exceção do código.
    '''
    composicao_a_alterar = Composicao.query.filter_by(codigo=codigo).first()
    composicao = request.get_json()
    if not composicao:
        return None
    # Altera os campos da composicao
    if composicao.get('descricao'):
        composicao_a_alterar.descricao = composicao['descricao']
    if composicao.get('grupo'):
        composicao_a_alterar.grupo = composicao['grupo']
    if composicao.get('custo_unitario'):
        composicao_a_alterar.custo_unitario = composicao['custo_unitario']
    if composicao.get('unidade'):
        composicao_a_alterar.unidade = composicao['unidade']
    # Salva alterações no banco de dados
    db.session.commit()
    return composicao


def remover_composicao(codigo):
    '''
    Remove uma composição do banco de dados.
    '''
    composicao_existente = Composicao.query.filter_by(codigo=codigo).first()
    if not composicao_existente:
        return None

    db.session.delete(composicao_existente)
    db.session.commit()

    # composicoes[indice].update(composicao)
# pprint(get_composicoes_by_codigo(104658))
