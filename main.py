# Flask para criar API's
# Tradicional ou Restfull
# pip install flask
from flask import Flask
from extensions import db
from router_composicao import composicao_rotas

SECRET_KEY = 'JKHJK5465324BJy*(&@JKH)'
# Criar uma API Flask
app = Flask(__name__)

# Criar uma instância de SQLAchemy
app.config['SECRET_KEY'] = SECRET_KEY
# connection string oracle
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///composicoes.db'

# Definir o objetivo da APIS: consultar, editar, criar e exluir composições em um banco de dados
db.init_app(app)
app.register_blueprint(composicao_rotas)

# URL base
if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)
