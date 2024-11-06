import sqlite3
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()
cursor.execute(''' DROP TABLE IF EXISTS clientes ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)
''')
cursor.execute('''
INSERT INTO clientes (nome, idade) VALUES ('Pedro Place', 22)
''')
cursor.execute('''
INSERT INTO clientes (nome, idade) VALUES ('Bruna Silva', 23)
''')
cursor.execute('''
INSERT INTO clientes (nome, idade) VALUES ('Matilde Braga', 25)
''')
conexao.commit()
cursor.execute('SELECT * FROM clientes')
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)
print( )
cursor.execute(''' DROP TABLE IF EXISTS produtos ''')
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
print( )
cursor.execute(''' DROP TABLE IF EXISTS compras ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
)
''')
cursor.execute('''
INSERT INTO compras (cliente_id, produto_id, quantidade) VALUES (1, 1, 2)
''')
cursor.execute('''
INSERT INTO compras (cliente_id, produto_id, quantidade) VALUES (2, 2, 1)
''')
cursor.execute('''
INSERT INTO compras (cliente_id, produto_id, quantidade) VALUES (3, 3, 3)
''')
conexao.commit()
cursor.execute('''
SELECT clientes.nome, produtos.nome, compras.quantidade
FROM compras
JOIN clientes ON compras.cliente_id = clientes.id
JOIN produtos ON compras.produto_id = produtos.id
''')
resultados = cursor.fetchall()
for linha in resultados:
    print(f"Cliente: {linha[0]}, Produto: {linha[1]}, Quantidade: {linha[2]}")
print( )
cursor.execute('''
ALTER TABLE compras ADD COLUMN data DATE
''')
cursor.execute('''
INSERT INTO compras (cliente_id, produto_id, quantidade, data) VALUES (1, 1, 2,'2024-10-15')
''')
cursor.execute('''
INSERT INTO compras (cliente_id, produto_id, quantidade, data) VALUES (2, 2, 1, '2024-10-20')
''')
cursor.execute('''
INSERT INTO compras (cliente_id, produto_id, quantidade, data) VALUES (3, 3, 3, '2024-11-01')
''')
cursor.execute('''
INSERT INTO compras (cliente_id, produto_id, quantidade, data) VALUES (1, 3, 1, '2023-11-05')
''')
conexao.commit()
cursor.execute('''
SELECT clientes.nome, produtos.nome, compras.data
FROM compras
JOIN clientes ON compras.cliente_id = clientes.id
JOIN produtos ON compras.produto_id = produtos.id
WHERE data>DATE('now', '-30 days')
''')
resultados = cursor.fetchall()
for linha in resultados:
    print(f"Cliente: {linha[0]}, Produto: {linha[1]}, Data: {linha[2]}")
conexao.close()