import sqlite3

# Conexão com a base de dados 'escola.db'
conexao = sqlite3.connect('escola.db')

# Criação de um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criação de uma tabela 'alunos' com os campos 'id', 'nome', 'idade' e
'curso'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        curso TEXT
        )
''')
# Inserir dados na tabela
cursor.execute('''
    INSERT INTO alunos(nome, idade, curso)
    VALUES ('João Silva', 20, 'Desenvolvimento Web')
    ''')
# Salvar (commit) as alterações na base de dados
conexao.commit()
# Consultar os dados inseridos
cursor.execute('SELECT * FROM alunos')
resultado = cursor.fetchall()
# Exibir os resultados
for linha in resultado:
    print(linha)
# Fechar a conexão com a base de dados
conexao.close()