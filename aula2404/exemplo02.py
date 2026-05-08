numeros = [] 
soma = 0

for i in range(10):
    num = int(input("Informe um numero: "))
    numeros.append(num)
maior = menor = numeros[0]
for num in numeros:
    print("Valor: ", num)
    soma += num
    if num > maior:
        maior = num    
    if num < menor:
        menor = num
media = soma/len(numeros)

print("Media:", media)
print("Maior: ",maior)
print("Menor:", menor) 

novo_numero = int(input("Informe um numero para saber se esta na lista:"))
    





