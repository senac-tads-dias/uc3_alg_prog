texto = input("Informe um texto: ")

cont = 0
for letra in texto:
    if letra.isdigit():
        cont += 1

print("O total de numeros e: ", cont)





