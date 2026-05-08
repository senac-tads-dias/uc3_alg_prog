def imprimirLista(lista):
    for num in lista:        
        print("Valor:", num)

def imprimirNumerosPar(lista):
    for num in lista: 
        if num%2 ==0:       
            print("Par:", num)


a = [2,5,3,6,3,78,4,3]
imprimirLista(a)
imprimirNumerosPar(a)
