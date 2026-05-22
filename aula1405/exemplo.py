
def EPrimo(P): 
    if P <= 1:
        return "Erro"
    elif P == 2: 
        return 1
    elif P % 2 == 0: # 3/2 calcula o resto da divisão 
        return 0
    else: #13
        raiz = P ** 0.5  # 15^0.5 = 3,87
        R = 1 
        i = 3
        while i <= raiz and R != 0: 
            R = P % i #15/3 => resto 0 ---> R = 0
            i+=2 #  i = 5
        return R #R = 0

lista_nprimos = []
n = int("Informe um numero")
EPrimo(n)












