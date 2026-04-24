numero = input("Informe um numero: ")
palindrome =  True
j = len(numero) - 1  #ultima posição da string
for i in  range(0, len(numero)//2):
    print("i: ", numero[i], "j: ", numero[j])
    if numero[i] != numero[j]:
        palindrome = False
        break
    j -= 1

if palindrome:
    print("O numero é palindrome")
else:
    print("O numero Não é palindrome")





