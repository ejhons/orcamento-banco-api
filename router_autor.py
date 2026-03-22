# Flask para criar API's
# Tradicional ou Restfull
# pip install flask
from flask import Flask, jsonify, request
import services  # import get_composicoes, get_composicoes_by_codigo, cria_composicao, altera_composicao, remover_composicao
app = Flask(__name__)
# dummy
# Definir o objetivo da APIS: consultar, editar, criar e exluir composições em um banco de dados

# URL base

# Rota padrão


@app.route('/')
def obter_composicoes():
    return jsonify(services.get_composicoes())
# Endpoints


@app.route('/composicoes/<int:codigo>', methods=['GET'])
def obter_composicao(codigo: int):
    return jsonify(services.get_composicoes_by_codigo(codigo))


@app.route('/composicoes', methods=['POST'])
def criar_composicao():
    composicao = request.get_json()
    services.cria_composicao(composicao)

    return jsonify(composicao, 200)


@app.route('/composicoes/<int:codigo>', methods=['PUT'])
def alterar_composicao(codigo: int):
    composicao_alterada = request.get_json()
    services.altera_composicao(codigo, composicao_alterada)

    return jsonify(composicao_alterada, 200)


@app.route('/composicoes/<int:codigo>', methods=['DELETE'])
def excluir_composicao(codigo):
    try:
        resultado = services.remover_composicao(codigo)
        if resultado:
            return jsonify({}, 200)
    except:
        pass

    return jsonify({'mensagem': 'Composição não econtrada.'}, 404)
# Recursos disponibilizados pela API

# Verbos a serem disponibilizados: GET, POST, PUT, DELETE

# URLs completos de cada um


app.run(port=5000, host='localhost', debug=True)
