def imprimeIdade(idade):
    if(idade >= 18):
        print("Maior de idade")
    else:
        print("Menor de idade")

idade = int(input("Digite sua idade: "))
imprimeIdade(idade)
