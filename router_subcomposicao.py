# Flask para criar API's
# Tradicional ou Restfull
# pip install flask
from flask import Blueprint, jsonify, request
from models import Composicao, Subcomposicao
from extensions import db
from services import get_subcomposicoes_completas
# from main import db
# import services  # import get_composicoes, get_composicoes_by_codigo, cria_composicao, altera_composicao, remover_composicao
# app = Flask(__name__)

subcomposicao_rotas = Blueprint('subcomposicao_rotas', __name__)
# Rota padrão


@subcomposicao_rotas.route('/composicoes/<int:codigo>/subcomposicoes', methods=['GET'])
def obter_subcomposicoes(codigo: int):
    composicao = Composicao.query.filter_by(codigo=codigo).first()

    if not composicao:
        return jsonify({'mensagem': f'{codigo} não encontrada'}, 401)

    resultado = []
    for sub in composicao.sub_composicoes:
        resultado.append({
            "codigo": sub.codigo,
            "coeficiente": sub.coeficiente
        })

    return jsonify({'composicao': codigo, 'subcomposicoes': resultado}, 200)


@subcomposicao_rotas.route('/composicoes/<int:codigo>/subcomposicoes_raw', methods=['GET'])
def obter_subcomposicoes_completas(codigo: int):
    resultado = get_subcomposicoes_completas(codigo=codigo)
    return jsonify(resultado, 200)


@subcomposicao_rotas.route('/composicoes/<int:codigo>/subcomposicoes/adicionar', methods=['POST'])
def criar_subcomposicoes_by_composicao(codigo: int):
    subcomposicoes = request.get_json()['subcomposicoes']
    for nova_sub in subcomposicoes:
        try:
            # Retornar erro se composição principal não for localizada
            subcomposicao = Subcomposicao(
                codigo=nova_sub['id'],
                id_composicao=codigo,
                coeficiente=float(nova_sub.get('coeficiente', 0.0))
            )
            db.session.add(subcomposicao)
        except Exception as e:
            print(e)
    db.session.commit()

    return jsonify({'mensagem': f'{len(subcomposicoes)} composições criadas com sucesso!'}, 200)


@subcomposicao_rotas.route('/subcomposicoes/adicionar', methods=['POST'])
def criar_subcomposicoes():
    subcomposicoes = request.get_json()['subcomposicoes']
    for nova_subcomposicao in subcomposicoes:
        try:
            subcomposicao = Subcomposicao(
                codigo=nova_subcomposicao['id'],
                id_composicao=nova_subcomposicao['id_composicao'],
                coeficiente=float(nova_subcomposicao.get('coeficiente', 0.0))
            )
            db.session.add(subcomposicao)
        except Exception as e:
            print(e)

    db.session.commit()

    return jsonify({'mensagem': f'{len(subcomposicoes)} composições criadas com sucesso!'}, 200)


@subcomposicao_rotas.route('/composicoes/<int:codigo>/subcomposicoes/<int:id_sub>', methods=['PUT'])
def alterar_coeficiente_subcomposicao(codigo: int, id_sub: int):
    # composicao_alterada = request.get_json()
    # services.altera_composicao(codigo, composicao_alterada)
    # return jsonify(composicao_alterada, 200)
    sub_alterar = Subcomposicao.query.filter_by(
        id_composicao=codigo, id=id_sub).first()
    sub = request.get_json()
    if not sub:
        return jsonify({'mensagem': f'Composicao ({codigo}) não encontrada'}, 401)
    # Altera os campos da composicao
    if sub.get('coeficiente'):
        sub_alterar.coeficiente = sub['coeficiente']
    # Salva alterações no banco de dados
    db.session.commit()
    return jsonify({'mensagem': f'{id_sub} da composição {codigo} alterada com sucesso!'}, 200)


@subcomposicao_rotas.route('/composicoes/<int:codigo>/subcomposicoes/<int:id_sub>', methods=['DELETE'])
def excluir_subcomposicao(codigo, id_sub):
    sub_existente = Subcomposicao.query.filter_by(
        id_composicao=codigo, id=id_sub).first()
    if not sub_existente:
        return jsonify({'mensagem': 'Composição não econtrada.'}, 404)
    db.session.delete(sub_existente)
    db.session.commit()

    return jsonify({'mensagem': f'subcomposição {id_sub} da composição {codigo} excluída com sucesso!'}, 200)


@subcomposicao_rotas.route('/composicoes/<int:codigo>', methods=['DELETE'])
def excluir_subcomposicoes(codigo):
    subs_existentes = Subcomposicao.query.filter_by(codigo=codigo)
    if not subs_existentes or len(subs_existentes) == 0:
        return jsonify({'mensagem': 'Composição não econtrada.'}, 404)
    for sub in subs_existentes:
        db.session.delete(sub)
    db.session.commit()

    return jsonify({'mensagem': f'{len(subs_existentes)} subcomposições da composição {codigo} excluídas com sucesso!'}, 200)
