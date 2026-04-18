#Faça um programa que utilize uma estrutura de repetição
#para ler números inteiros digitados pelo usuário. 
# O programa deve continuar solicitando valores até que o 
# usuário digite o número 0 (zero), que servirá como condição 
# de parada.
#Ao final, o programa deve apresentar:
#A quantidade total de números digitados (desconsiderando o zero);
#A soma de todos os valores informados;
#O maior valor digitado.

numero = 1
qtd = 0
soma = 0
maior = 0
menor = 0
while numero != 0:
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

print("Processando as informações")
print("A quantidade total é: ", qtd)
print("A soma total é: ", soma)
print("O maior numero é: ", maior)
print("O menor numero é: ", menor)



