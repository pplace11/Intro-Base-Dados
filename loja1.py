import sqlite3
conexao = sqlite3.connect('loja1.db')
cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    preco REAL
)
''')
cursor.execute('''
INSERT INTO produtos (nome, preco) VALUES ('Caneta', 1.50)
''')
cursor.execute('''
INSERT INTO produtos (nome, preco) VALUES ('Lapis', 1.40)
''')
cursor.execute('''
INSERT INTO produtos (nome, preco) VALUES ('Caderno', 3.75)
''')
conexao.commit()
cursor.execute('SELECT * FROM produtos')
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)
conexao.close()