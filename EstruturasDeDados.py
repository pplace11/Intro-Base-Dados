# Lista e Tupas --- estruturas de dados ORDENADAS
#users = ("Tiago", "Ana")
#user = ["Tiago", "Ana"]
#user[1] = 'Joana'
#users[1] = 'Joana' não pode fazer
#print(users)
#print(type(users))
#print(user)
#print(type(user))
#user = user + ["Rita"] igual o de baixo
#user += ["Rita"]
users = ['Tiago', 'Ana', 'Rita', 'Ricardo', 'Joana']
for user in users:
    age = input("Indicar idade: ")
    print(f"O {user} tem {age} anos.")