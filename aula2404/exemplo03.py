numeros = [] 

for i in range(10):
    num = int(input("Informe um numero: "))
    numeros.append(num)

novo_numero = int(input("Informe um numero para saber se esta na lista:"))

# achou = False   
# for num in numeros:
#     if novo_numero == num:
#         achou = True
# if achou:
#     print("O numero foi encontrado")
# else:
#     print("O numero não foi encontrado")

if novo_numero in numeros:
    print("O numero foi encontrado") 
else:
    print("O numero não foi encontrado")




