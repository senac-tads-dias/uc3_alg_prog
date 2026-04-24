'''7. Crie um programa que simule um caixa eletrônico, mostrando a quantidade mínima de
notas para um saque (100, 50, 20, 10, 5, 2).'''

valor = int(input("Informe um valor para saque: "))

if valor%2 == 0 or valor%5 == 0:     
    if valor >= 100:
        nota100 = valor//100
        restante = valor - nota100*100
        print("Total nota de 100: ", nota100)

    if restante >= 50:
        nota50 = restante//50 
        restante = restante - nota50*50
        print("Total nota de 50: ", nota50)

    if restante >= 20:
        nota20 = restante//20 
        restante = restante - nota20*20
        print("Total nota de 20: ", nota20)

    if restante >= 10:
        nota10 = restante//10 
        restante = restante - nota10*10
        print("Total nota de 10: ", nota10)

    if restante % 5 == 0:
        nota5 = restante//5 
        restante = restante - nota5*5
        print("Total nota de 5: ", nota5)

    if restante % 2 == 0 and restante >= 2:
        nota2 = restante//2 
        restante = restante - nota2*2 
        print("Total nota de 2: ", nota2)
else:
    print("Este caixa não pode sacar esse valor que vc deseja!")


