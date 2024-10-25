import sqlite3

conexao = sqlite3.connect('school.db')
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS aluno(
        id INTERGER PRIMARY KEY,
        nome TEXT,
        idade INTERGER,
        curso TEXT
        )
''')
cursor.execute('''
    INSERT INTO aluno (nome, idade, curso)
    VALUES ('Pedro', 22, 'Desenvolvimento Web')
''')
cursor.execute('''
    INSERT INTO aluno (nome, idade, curso)
    VALUES ('Ana Costa', 21, 'Desenvolvimento Web')
''')
cursor.execute('''
    INSERT INTO aluno (nome, idade, curso)
    VALUES ('Carlos Sousa', 22, 'Desenvolvimento Web')
''')
conexao.commit()
cursor.execute('''
    UPDATE aluno
    SET idade = 23
    WHERE nome = 'Ana Costa'
''')
cursor.execute ('SELECT * FROM aluno')
resultados = cursor.fetchall()
print("\n Dados após a inserção e atualização: ")
for linha in resultados:
    print(linha)
cursor.execute('''
    DELETE FROM aluno
    WHERE nome = 'Carlos Sousa'
''')
conexao.commit()
cursor.execute ('SELECT * FROM aluno')
resultado = cursor.fetchall()
print("\n Dados após remoção: ")
for linha in resultado:
    print(linha)
conexao.close()