
#num = int(input("Informe um numero para saber se ele é um numero perfeito: "))
for num_teste in range(1, 1000):
    num = num_teste
    soma = 0
    for index in range(1, num):
        if num % index == 0:
            soma += index # soma = soma + index

    if soma == num:
        print("O numero é perfeito: ", num)
    #else:
        #print("O numero Não é perfeito!")

