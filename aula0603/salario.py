qtdHoras = int(input("Informe a qtd de horas trabalhadas: ")) 
valorHora = float(input("Informe o valor da hora trabalhada: "))

if qtdHoras <= 160:
    salario = qtdHoras*valorHora
    print("O salario é: ", salario)
else:
    horaExtra = qtdHoras - 160
    salarioExtra = horaExtra*valorHora*1.5
    salario = (160 * valorHora) + salarioExtra 
    print("O salario é: ", salario)
    print("O salario extra: ", salarioExtra)
     






