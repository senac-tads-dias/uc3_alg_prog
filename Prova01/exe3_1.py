
qtd = 0
soma = 0
maior = 0
menor = 0
while True:
    numero = int(input("Informe um numero inteiro: "))
    if numero != 0:
        #Contando a qtd de numeros digitados
        qtd = qtd + 1  #qtd += 1 
        soma = soma + numero #soma += numero

        if numero > maior:
            maior = numero 

        if qtd == 1:
            menor = numero
        elif numero < menor:
            menor = numero
    else:
        break     

print("Processando as informações")
print("A quantidade total é: ", qtd)
print("A soma total é: ", soma)
print("O maior numero é: ", maior)
print("O menor numero é: ", menor)