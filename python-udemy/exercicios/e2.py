def aprovacao(n1, n2):
    if(media >= 6):
        print("Aprovado")
    else:
        print("Reprovado")

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
media = (n1 + n2)/2

aprovacao(n1, n2)