import sqlite3
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)
''')
cursor.execute('''
INSERT INTO clientes (id, nome, idade) VALUES (1, 'Pedro Place', 22)
''')
cursor.execute('''
INSERT INTO clientes (id, nome, idade) VALUES (2, 'Bruna Silva', 23)
''')
cursor.execute('''
INSERT INTO clientes (id, nome, idade) VALUES (3, 'Matilde Braga', 25)
''')
conexao.commit()
cursor.execute('SELECT * FROM clientes')
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)
conexao.close()