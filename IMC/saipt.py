import sqlite3

conn = sqlite3.connect('saipt.db')
cursor = conn.cursor()

#Criar tabela de usuario
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    altura FLOAT NOT NULL,
    peso FLOAT NOT NULL
)
''')
conn.commit()

#Funçao de registro
def resgistrar_usuario(nome, idade, altura, peso):
    cursor.execute('''
    INSERT INTO usuarios (nome, idade, altura, peso) VALUES (?, ?, ?, ?)
    ''', (nome, idade, altura, peso))
    conn.commit()
    print(f"Usuário {nome} registrado com sucesso!")

#Soliciatar dados
for i in range(1):
    print(f"\nInsira os dados do usuário {i+1}:")
    nome = input("Diga o seu nome: ")
    idade = int(input("Diga a sua idade: "))
    altura = float(input("Diga a sua altura(metros): "))
    peso = float(input("Diga o seu peso(kg): "))
    resgistrar_usuario(nome, idade,altura, peso)

#Funçao para calcular o IMC
def consultar_usuario(nome):
    cursor.execute('''
    SELECT nome, idade, altura, peso FROM usuarios WHERE nome = ?
    ''', (nome,))
    usuario = cursor.fetchone()
    if usuario:
        nome_usuario = usuario[0]
        idade = usuario[1]
        altura = usuario[2]
        peso = usuario[3]
        imc = peso / (altura**2)
        dados_usuario = f"\nNome: {nome}\nIdade: {idade}\nAltura: {altura} m\nPeso: {peso} kg\nIMC: {imc:.2f}"
        print(dados_usuario)
        #Escrever os dados em arquivos de texto
        with open('usuario_consulta.txt', 'w') as file:
            file.write(dados_usuario)
            print(f"Dados do usuário {nome_usuario} foram salvos em 'usuario_consultado.txt'.")
    else:
        print(f"Usuario {nome} não encontrado.")

#Consulta de um usuario pelo nome
nome_para_consultar = input("\nDigite o nome do usuário que deseja ser consultado: ")
consultar_usuario(nome_para_consultar)
conn.close()