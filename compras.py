import sqlite3
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()
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
conexao.close()