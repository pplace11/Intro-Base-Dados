import sqlite3

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()
cursor.execute(''' DROP TABLE IF EXISTS livros ''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY,
        title TEXT,
        autor TEXT,
        ano INTEGER
        )
''')
cursor.execute('''
    INSERT INTO livros (title, autor, ano)
    VALUES ('Harry Potter e a Pedra Filosofal', 'K. Rowling', 1997)
''')
cursor.execute('''
    INSERT INTO livros (title, autor, ano)
    VALUES ('Harry Potter e a Câmara Secreta', 'K. Rowling', 1998)
''')
cursor.execute('''
    INSERT INTO livros (title, autor, ano)
    VALUES ('Harry Potter e o Prisioneiro de Azkaban', 'K. Rowling', 1999)
''')
cursor.execute('''
    INSERT INTO livros (title, autor, ano)
    VALUES ('Harry Potter e o Cálice de Fogo', 'K. Rowling', 2000)
''')
cursor.execute('''
    INSERT INTO livros (title, autor, ano)
    VALUES ('Harry Potter e a Ordem da Fênix', 'K. Rowling', 2003)
''')
cursor.execute('''
    INSERT INTO livros (title, autor, ano)
    VALUES ('Harry Potter e o Enigma do Príncipe', 'K. Rowling', 2005)
''')
cursor.execute('''
    INSERT INTO livros (title, autor, ano)
    VALUES ('Harry Potter e as Relíquias da Morte', 'K. Rowling', 2007)
''')
cursor.execute('''
    INSERT INTO livros (title, autor, ano)
    VALUES ('Harry Potter e a Criança Amaldiçoada', 'K. Rowling', 2016)
''')
conexao.commit()
cursor.execute('SELECT * FROM livros')
resultado = cursor.fetchall()
for linha in resultado:
    print(linha)
conexao.close()