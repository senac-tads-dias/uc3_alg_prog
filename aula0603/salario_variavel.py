# se passou de 200 horas
qtdHoras = int(input("Informe a qtd de horas trabalhadas: ")) 
valorHora = float(input("Informe o valor da hora trabalhada: "))

if qtdHoras <= 160: #Horas menor igual a 160
    salario = qtdHoras*valorHora
    print("O salario é: ", salario)
elif qtdHoras > 160 and qtdHoras <= 200: #Horas maior que 160 e menor igual que 200
    horaExtra = qtdHoras - 160
    salarioExtra = horaExtra*valorHora*1.5
    salario = (160 * valorHora) + salarioExtra 
    print("O salario é: ", salario)
    print("O salario extra: ", salarioExtra)
else:
    print("A qtd de horas não pode ultrapassar as 200 horas")

#fim do algoritmo