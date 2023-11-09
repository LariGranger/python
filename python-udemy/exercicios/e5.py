n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))
sinal = input("sinal: ")

if(sinal == '+'):
    soma = n1 + n2
    print(soma)
elif(sinal == '-'):
    sub = n1 - n2
    print(sub)
elif(sinal == '*'):
    mult = n1 * n2
    print(mult)
elif(sinal == '/'):
    div = n1 / n2
    print(div)
