import sqlite3
import tkinter as tk
from tkinter import messagebox

#Abrir conexão
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
    messagebox.showinfo("Sucesso", f"Usuário {nome} registrado com sucesso!")

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
        messagebox.showinfo("Dados do usuário", dados_usuario)
        #Escrever os dados em arquivos de texto
        with open('usuario_consulta.txt', 'w') as file:
            file.write(dados_usuario)
        messagebox.showinfo("Sucesso", f"Dados do usuário {nome_usuario} foram salvo em 'usuario_consulta.txt'.")
    else:
        messagebox.showinfo("Erro", f"Usuário {nome} não encontrado.")

#Configurar a interface gráfica
root = tk.Tk()
root.title("Registro de usuário")

#Frame para registrar
frame_registro = tk.Frame(root)
frame_registro.pack(pady=10)

tk.Label(frame_registro, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame_registro, text="Idade:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(frame_registro, text="Altura (m):").grid(row=2, column=0, padx=5, pady=5)
tk.Label(frame_registro, text="Peso (kg):").grid(row=3, column=0, padx=5, pady=5)

nome_entry = tk.Entry(frame_registro)
idade_entry = tk.Entry(frame_registro)
altura_entry = tk.Entry(frame_registro)
peso_entry = tk.Entry(frame_registro)

nome_entry.grid(row=0, column=0, padx=5, pady=5)
idade_entry.grid(row=1, column=0, padx=5, pady=5)
altura_entry.grid(row=2, column=0, padx=5, pady=5)
peso_entry.grid(row=3, column=0, padx=5, pady=5)

def registrar_usuario_tk():
    nome = nome_entry.get()
    idade = int(idade_entry.get())
    altura = float(altura_entry.get())
    peso = float(peso_entry.get())
    resgistrar_usuario(nome, idade, altura, peso)

tk.Button(frame_registro, text="Registrar", command=registrar_usuario_tk).grid(row=4, columnspan=2, pady=10)

#Frame de consulta
frame_consulta = tk.Frame(root)
frame_consulta.pack(pady=10)

tk.Label(frame_consulta, text="Nome para consulta:").grid(row=0, columnspan=2, pady=10)
nome_consulta_entry = tk.Entry(frame_consulta)
nome_consulta_entry.grid(row=0, column=1, padx=5, pady=5)

def consulta_usuario_tk():
    nome = nome_consulta_entry.get()
    consultar_usuario(nome)

tk.Button(frame_consulta, text="Consulta", command=consulta_usuario_tk).grid(row=1, columnspan=2, pady=10)

#Iniciar a interface gráfica
root.mainloop()

#Fechar conexão
conn.close()
