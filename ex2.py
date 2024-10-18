pwds, pwd =  1, "Almada_Lisboa"
for pwds in range(3):
    guess = input("Qual a senha? ")
    print(guess)
    if guess == pwd:
        print(f"Correto!")
        break
    else:
        print(f"Errado")
print(f'Fim de jogo, com {pwds+ 1} tentativas')