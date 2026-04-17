operacao = 1

while operacao > 0:

    #menu
    print("************************")
    print("*      MENU            *")
    print("*  1 - SOMAR           *")
    print("*  2 - SUBTRAIR        *")
    print("*  3 - MULTIPLICAR     *")
    print("*  4 - DIVIDIR         *")
    print("*  0 -  SAIR           *")
    print("************************")

    operacao = int(input("Informe o valor da operação: "))
    valor1 = int(input("Informe o valor 1: "))
    valor2 = int(input("Informe o valor 2: "))

    if operacao == 1:
        print("\nA Soma é: ", valor1+valor2)
    elif operacao == 2:
        print("\nA Subtração é: ", valor1-valor2)
    elif operacao == 3:
        print("\nA Multiplicação é: ", valor1*valor2)
    elif operacao == 4:
        print("\nA Divisão é: ", valor1/valor2)
    elif operacao == 0:
        print("\nSaindo...")
    else:
        print("\nOpção inválida")





