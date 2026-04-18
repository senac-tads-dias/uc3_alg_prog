'''Faça um programa que receba o código correspondente ao cargo de um funcionário 
e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão na tabela abaixo. 
Código  Cargo           Percentual 
1	    Escriturário 	50% 
2	    Secretário	    35%
3 	    Caixa		    20% 
4 	    Gerente 	    10% 
5 	    Diretor 	    Não tem aumento '''

print("Informe o Codigo correspondente")
print('''Código      Cargo      
    1	    Escriturário 	
    2	    Secretário	    
    3 	    Caixa		   
    4 	    Gerente 	    
    5 	    Diretor \n''')
codigo = int(input("Codigo: "))
salario = float(input("Informe o seu salário atual: "))

if codigo == 1:
    print("Cargo de Escriturário")
    valor_aumento = salario * 0.5
    novo_salario = valor_aumento + salario
    print("Valor do aumento é: ", valor_aumento)
    print("O novo salario é: ", novo_salario)

elif codigo == 2:
    print("Cargo de Secretário")
    valor_aumento = salario * 0.35
    novo_salario = valor_aumento + salario
    print("Valor do aumento é: ", valor_aumento)
    print("O novo salario é: ", novo_salario)

elif codigo == 3:
    print("Cargo de Caixa")
    valor_aumento = salario * 0.2
    novo_salario = valor_aumento + salario
    print("Valor do aumento é: ", valor_aumento)
    print("O novo salario é: ", novo_salario)

elif codigo == 4:
    print("Cargo de Gerente") 
    valor_aumento = salario * 0.1
    novo_salario = valor_aumento + salario
    print("Valor do aumento é: ", valor_aumento)
    print("O novo salario é: ", novo_salario)

elif codigo == 5:
    print("Cargo de Diretor")    
    print("Não tem aumento!")
    print("O seu salario é: ", salario)

else:
    print("Codigo inválido")






