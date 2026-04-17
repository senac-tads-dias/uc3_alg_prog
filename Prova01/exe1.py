#Faça um programa para receber valores inteiros 
# X, Y e Z do usuário e apresente o maior e o menor valor. 
x = int(input("Informe o valor de X: "))
y = int(input("Informe o valor de Y: "))
z = int(input("Informe o valor de Z: "))

if x > y and y > z:
    print("O X é Maior e o Z é o Menor")
elif x > z and z > y:
    print("O X é Maior e o Y é o Menor")
elif y > x and x > z:
    print("O Y é Maior e o Z é o Menor")
elif y > z and z > x:
    print("O Y é Maior e o X é o Menor")
elif z > x and x > y:
    print("O Z é Maior e o Y é o Menor")
elif z > y and y > x:
    print("O Z é Maior e o X é o Menor")
else:
    print("Existe numeros iguais-")

    
    




