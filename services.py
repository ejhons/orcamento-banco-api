
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


def get_composicao_by_codigo(codigo):
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
    pares = Subcomposicao.query.filter_by(id_composicao=codigo)
    if not pares:
        return None

    subcomposicoes = []
    for par in pares:
        nova_subcomposicao = get_composicao_by_codigo(par.codigo)
        if nova_subcomposicao:
            # print(f'Antes:{nova_subcomposicao}')
            nova_subcomposicao['coeficiente'] = par.coeficiente
            # print(f'---\nDepois{nova_subcomposicao}')
            subcomposicoes.append(nova_subcomposicao)
            # print(f'{par.codigo} coeficiente = {par.coeficiente}')
        else:
            print(f'{par.codigo} não encontrado!')
        # try:
        #     if not nova_subcomposicao:
        #         print(f'{par.codigo} não encontrado!')
        #         continue
        #     # Atualiza o coeficiente da subcomposicao
        #     nova_subcomposicao['coeficiente'] = par.coeficiente
        #     subcomposicoes.append(nova_subcomposicao)
        # except:
        #     print(f'{par.codigo} não encontrado!')

    return subcomposicoes


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


def is_insumo(codigo: int) -> bool:
    return Subcomposicao.query.filter_by(id_composicao=codigo).first() == None


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


def get_subcomposicoes_completas(codigo: int = None, composicao=None):
    if not (codigo or composicao):
        return {}
    if codigo:
        composicao = get_composicao_by_codigo(codigo)
    else:
        codigo = composicao['codigo']
    composicao['coeficiente'] = composicao.get('coeficiente', 1.0)

    subcomposicoes = get_subcomposicoes(codigo)

    lista = []
    for subcomposicao in subcomposicoes:
        lista.append(get_subcomposicoes_completas(composicao=subcomposicao))

    return {
        'composicao': composicao,
        'subcomposicoes': lista
    }
