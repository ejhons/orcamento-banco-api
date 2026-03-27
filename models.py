from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import db


class Composicao(db.Model):
    '''
    Tabela principal de composições.
    columns = [codigo, descricao, grupo, custo_unitario, unidade]
    TODO: Implementar colunas de informação da fonte.
    '''
    __tablename__ = 'composicoes'
    codigo = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, nullable=False)
    grupo = db.Column(db.String, nullable=False)
    custo_unitario = db.Column(db.Float, nullable=False)
    unidade = db.Column(db.String, nullable=False)
    coeficiente = db.Column(db.Float, default=1.0)

    sub_composicoes_mae = db.relationship(
        'Subcomposicao',
        foreign_keys='Subcomposicao.codigo',
        backref='composicao_mae'
    )
    sub_composicoes = db.relationship(
        'Subcomposicao',
        foreign_keys='Subcomposicao.id_composicao',
        backref='composicao_filha'
    )


class Subcomposicao(db.Model):
    '''
    Tabela de subcomposições utilizadas no detalhamento do orçamento quanto à composição do custo.
    [codigo_subcomposicao*,codigo_composicao_mae*,coeficiente,custo_unitario**,unidade**]
    As colunas de código marcadas com * precisarão funcionar como uma dupla chave que ainda preciso ver como fazer. 
    As colunas de custo_unitario e unidade (marcadas com **) são dispensáveis já que sua existência causaria
    ambiguidade/duplicidade de informações.
    '''
    __tablename__ = 'subcomposicoes'
    # db.ForeignKey('nome_tabela.coluna')
    codigo = db.Column(
        db.Integer,
        db.ForeignKey('composicoes.codigo'),
        primary_key=True)
    id_composicao = db.Column(
        db.Integer,
        db.ForeignKey('composicoes.codigo'),
        primary_key=True)
    coeficiente = db.Column(db.Float, nullable=False)

    # # (Opcional) acessar diretamente os objetos
    # composicao1 = db.relationship(
    #     'Composicao',
    #     foreign_keys=[codigo]
    # )

    # composicao2 = db.relationship(
    #     'Composicao',
    #     foreign_keys=[id_composicao]
    # )


class Usuario(db.Model):
    '''
    Tabela de usuário para acesso à informação da API. 
    A ser usado apenas para garantir que nenhum usuário poderá alterar o banco de dados de forma arbitrária
    '''
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)  # , auto_increment=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    admin = db.Column(db.Boolean, default=False)
