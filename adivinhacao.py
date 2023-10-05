print('********************************')
print("Bem vindo ao jogo de adivinhação")
print('********************************')

numero_secreto = 35

chute = int(input("Digite o seu número: "))
print("Voce digitou", chute)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    if(chute > numero_secreto):
        print("Você errou, seu chute foi maior qu o número secreto")
    elif(chute < numero_secreto):
        print("Você errou, seu chute foi menor qu o número secreto")

print("Fim de jogo!")