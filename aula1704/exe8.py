ultimo_valor = 0
crescente = True
while True:
    valor = int(input("Informe um numero ou digite 0 para parar: "))

    if valor == 0:
        break
    elif ultimo_valor > valor:
        crescente = False
    else:
        ultimo_valor = valor

if crescente:
    input("A sequencia é crescente!")
else:
    input("A sequencia Não é crescente!")


