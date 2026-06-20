
try:
    a = int(input("Informe um numero"))
    b = int(input("Informe um numero"))
    c = a/b
    
except IndexError:
    print("Erro posição da lista")
except ValueError:
    print("Valor inserido não converte")
except ZeroDivisionError:
    print("Valor não divisivel por zero")
except:
    print("Outro erro")








