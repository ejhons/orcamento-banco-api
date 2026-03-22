import sqlite3

with sqlite3.connect('composicoes.db') as conexao:
    # Cria uma conexão com o banco de dados
    sql = conexao.cursor()
    # Rodando comando SQL
    sql.execute(
        'CREATE TABLE COMPOSICOES(codigo interger, descricao text, grupo_1 text, custo_unitario float, unidade text);'
    )
    # Exemplo de inserir dados
    sql.execute(
        'INSERT INTO COMPOSICOES(codigo, descricao, grupo_1, custo_unitario, unidade) VALUES (123.6, "Primeira Descrição", "Composições", "15.50", "unid");'
    )
    # Exemplo de usar dados da aplicação em uma aplicação SQL
    dado = [123456, 'Descrição simples', 'Grupo 1', 60.50, 'm']
    sql.execute('INSERT INTO COMPOSICOES VALUES(?,?,?,?,?);', dado)

    conexao.commit()

    # Exibir dados no console
    composicoes = sql.execute('SELECT * FROM COMPOSICOES;')
    for composicao in composicoes:
        print(composicao)
