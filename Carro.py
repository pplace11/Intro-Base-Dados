import sqlite3
conexao=sqlite3.connect('carro.db')
# 'car'
cursor=conexao.cursor()
cursor.execute('DROP TABLE IF EXISTS marcas')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS marcas (
        id INTEGER PRIMARY KEY,
        marca TEXT,
        modelos TEXT
        )
    ''')
cursor.execute('''
 INSERT INTO marcas(marca, modelos)
 VALUES('Opel', 'Silverato')
''')
cursor.execute('''
 INSERT INTO marcas(marca, modelos)
 VALUES('BMW', 'X3')
''')
cursor.execute('''
 INSERT INTO marcas(marca, modelos)
 VALUES('VW', 'Id.4')
''')
cursor.execute('''
 INSERT INTO marcas(marca, modelos)
 VALUES('VW', 'Id.5')
''')
conexao.commit()
cursor.execute('SELECT * FROM marcas')
resultado = cursor.fetchall()
for linha in resultado:
    print(linha)
# 'pessoas'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS comprador(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        valor INTEGER,
        mes TEXT
        )
    ''')
cursor.execute('''
    INSERT INTO comprador(nome, valor, mes)
    VALUES('Pedro', 30000, 'Novembro')
    ''')
conexao.commit()
cursor.execute('SELECT * FROM comprador')
resultado = cursor.fetchall()
for linha in resultado:
    print(linha)
conexao.close()