#Um posto está vendendo combustíveis com a seguinte tabela de descontos:  

#Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte 
# forma: A -  álcool. G - gasolina) e o valor do combustível, 
# calcule e imprima o valor a ser pago pelo cliente. 
litros = float(input("Informe a quantidade de litros: "))
tipo = input("Informe o tipo de combustivel: \nA para álcool\nG para gasolina \nOpção: ")
valor = float(input("Informe o valor do combustivel selecionado: "))

# Álcool:
#Até 20 litros: desconto de 3% por litro
#Acima de 20 litros: Desconto de 5% por litro.
if tipo == "A" or tipo == "a":
    if litros <= 20.0:
        valor_total = (valor * litros) * 0.97
        print("O valor a ser pago é: ", round(valor_total, 2))
    else:
        valor_total = (valor * litros) * 0.95
        print("O valor a ser pago é: ", round(valor_total, 2))
        
#Gasolina:
#Até 20 litros: desconto de 4% por litro
#Acima de 20 litros, desconto de 6% por litro
if tipo == "G" and litros <= 20.0:
    valor_total = (valor * litros) * 0.96
    print("O valor a ser pago é: ", round(valor_total, 2))
elif tipo == "G" and litros > 20.0:
    valor_total = (valor * litros) * 0.94
    print("O valor a ser pago é: ", round(valor_total, 2))

