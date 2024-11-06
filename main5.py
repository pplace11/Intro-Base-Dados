import sqlite3
conexao = sqlite3.connect('main5.db')
cursor = conexao.cursor()

cursor.execute(''' DROP TABLE IF EXISTS livros ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER PRIMARY KEY,
    titulos TEXT,
    autor TEXT
)''')
cursor.execute(''' DROP TABLE IF EXISTS membros ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS membros(
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade TEXT
)''')
cursor.execute(''' DROP TABLE IF EXISTS emprestimos ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS emprestimos(
    id INTEGER PRIMARY KEY,
    livro_id INTEGER,
    membro_id INTEGER,
    data_emprestimo DATE,
    data_devolucao DATE,
    FOREIGN KEY (livro_id) REFERENCES livros(id),
    FOREIGN KEY (membro_id) REFERENCES membros(id)
)''')

cursor.execute('''
    INSERT INTO livros (titulos, autor) VALUES ('Harry Potter e a Pedra Filosofal', 'K. Rowling')
''')
cursor.execute('''
    INSERT INTO livros (titulos, autor) VALUES ('Harry Potter e a Câmara Secreta', 'K. Rowling')
''')
cursor.execute('''
    INSERT INTO livros (titulos, autor) VALUES ('Harry Potter e o Prisioneiro de Azkaban', 'K. Rowling')
''')
cursor.execute('''
    INSERT INTO membros (nome, idade) VALUES ('Pedro', 22)
''')
cursor.execute('''
    INSERT INTO membros (nome, idade) VALUES ('Bruna', 25)
''')
cursor.execute('''
    INSERT INTO membros (nome, idade) VALUES ('Sara', 19)
''')
cursor.execute('''
INSERT INTO emprestimos (livro_id, membro_id, data_emprestimo, data_devolucao) VALUES (1, 1, '2023-11-01', NULL)
''')
cursor.execute('''
INSERT INTO emprestimos (livro_id, membro_id, data_emprestimo, data_devolucao) VALUES (2, 2, '2023-11-02', NULL)
''')
cursor.execute('''
INSERT INTO emprestimos (livro_id, membro_id, data_emprestimo, data_devolucao) VALUES (3, 3, '2023-11-03', NULL)
''')
cursor.execute('''
INSERT INTO emprestimos (livro_id, membro_id, data_emprestimo, data_devolucao) VALUES (1, 2, '2023-11-01', '2023-11-12')
''')
conexao.commit()

cursor.execute('SELECT * FROM livros')
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)
print( )
cursor.execute('SELECT * FROM membros')
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)
print( )
cursor.execute('''
SELECT membros.nome, livros.titulos, emprestimos.data_emprestimo, emprestimos.data_devolucao
FROM emprestimos
JOIN membros ON emprestimos.membro_id = membros.id
JOIN livros ON emprestimos.livro_id = livros.id
WHERE emprestimos.data_devolucao IS NULL
''')
resultados = cursor.fetchall()
print("Livros atualmente emprestados: ")
for linha in resultados:
    print(f"Membro: {linha[0]}, Livro: {linha[1]}, Data de Emprestimo: {linha[2]}")

conexao.close()