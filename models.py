from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import db
# Definir estrutra da tabela de composições
# codigo, descricao, grupo, custo_unitario, unidade


class Composicao(db.Model):
    __tablename__ = 'composicoes'
    codigo = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String)
    grupo = db.Column(db.String)
    custo_unitario = db.Column(db.Float)
    unidade = db.Column(db.String)

    composicoes = db.relationship('Subcomposicao')


class Subcomposicao(db.Model):
    __tableaname__ = 'subcomposicoes'
    codigo = db.Column(db.Integer, primary_key=True)
    # db.ForeignKey('nome_tabela.coluna')
    id_composicao = db.Column(db.Integer, db.ForeignKey('composicoes.codigo'))
