# Flask para criar API's
# Tradicional ou Restfull
# pip install flask
from flask import Blueprint, jsonify, request
from models import Composicao, Subcomposicao
from extensions import db
# from main import db
# import services  # import get_composicoes, get_composicoes_by_codigo, cria_composicao, altera_composicao, remover_composicao
# app = Flask(__name__)
# dummy
# Rota padrão
composicao_rotas = Blueprint('composicao_rotas', __name__)


@composicao_rotas.route('/')
def obter_composicoes():
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

    return jsonify({'composicoes': lista_composicoes})
    # return jsonify(services.get_composicoes())

# Endpoints


@composicao_rotas.route('/composicoes/<int:codigo>', methods=['GET'])
def obter_composicao(codigo: int):
    composicao = Composicao.query.filter_by(codigo=codigo).first()
    if not composicao:
        return jsonify({'mensagem': f'{codigo} não encontrada'}, 401)

    nova_composicao = {}
    nova_composicao['codigo'] = composicao.codigo
    nova_composicao['descricao'] = composicao.descricao
    nova_composicao['grupo'] = composicao.grupo
    nova_composicao['custo_unitario'] = composicao.custo_unitario
    nova_composicao['unidade'] = composicao.unidade

    return jsonify({'composicao': nova_composicao}, 200)

    # return jsonify(services.get_composicoes_by_codigo(codigo))


@composicao_rotas.route('/composicoes/adicionar', methods=['POST'])
def criar_composicao():
    # composicao = request.get_json()
    # services.cria_composicao(composicao)
    # return jsonify(composicao, 200)

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

    return jsonify({'mensagem': f'{composicao.codigo} criada com sucesso!'}, 200)


@composicao_rotas.route('/composicoes/adicionar_varias', methods=['POST'])
def criar_composicoes():
    # composicao = request.get_json()
    # services.cria_composicao(composicao)
    # return jsonify(composicao, 200)

    composicoes = request.get_json()['composicoes']
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

    return jsonify({'mensagem': f'{len(composicoes)} composições criadas com sucesso!'}, 200)


@composicao_rotas.route('/composicoes/<int:codigo>', methods=['PUT'])
def alterar_composicao(codigo: int):
    # composicao_alterada = request.get_json()
    # services.altera_composicao(codigo, composicao_alterada)
    # return jsonify(composicao_alterada, 200)
    composicao_a_alterar = Composicao.query.filter_by(codigo=codigo).first()
    composicao = request.get_json()
    if not composicao:
        return jsonify({'mensagem': f'Composicao ({codigo}) não encontrada'}, 401)
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
    return jsonify({'mensagem': f'{codigo} alterada com sucesso!'}, 200)


@composicao_rotas.route('/composicoes/<int:codigo>', methods=['DELETE'])
def excluir_composicao(codigo):
    # try:
    #     resultado = services.remover_composicao(codigo)
    #     if resultado:
    #         return jsonify({}, 200)
    # except:
    #     pass

    # return jsonify({'mensagem': 'Composição não econtrada.'}, 404)

    composicao_existente = Composicao.query.filter_by(codigo=codigo).first()
    if not composicao_existente:
        return jsonify({'mensagem': 'Composição não econtrada.'}, 404)
    db.session.delete(composicao_existente)
    db.session.commit()

    return jsonify({'mensagem': f'{codigo} excluído com sucesso!'}, 200)


# Recursos disponibilizados pela API

# Verbos a serem disponibilizados: GET, POST, PUT, DELETE

# URLs completos de cada um
