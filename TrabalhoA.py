nome, idade, cores = [], [], []
count = 0
contador = 'Azul'
idademax = '20'
countidade = 0
for user in range(3):
    nome += input('Qual é o seu nome? ')
    idade = input('Qual a sua idade? ')
    cor = input('Qual a sua cor favorita? ')
    cores = cores + [cor]
    if cor == contador:
        count += 1
    if idade > idademax and cor == contador:
        countidade += 1
    print('\nUtilizador Registrado\n----------\n')
print(f"O número de pessoas que gostam de azul foi {count}.")
print(f"O número de pessoas que tem mais de 20 anos são {countidade}.")
