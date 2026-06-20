import ast

usuarios = []
def salvarUsuario(usuario):
    arquivo = open("aula1106/usuario.txt", "a")
    arquivo.write(str(usuario))
    arquivo.write("\n")
    arquivo.close()

def lerUsuarios():
    arquivo = open("aula1106/usuario.txt", "r")
    for linha in arquivo:        
        user = ast.literal_eval(linha)
        usuarios.append(user)
    arquivo.close()

while True:

    nome = input("Informe o nome para cadastro: ")
    if nome == "fim":
        break
    else:
        user = {}
        user["nome"] = nome
        user["idade"] = int(input("Informe a sua idade: "))
        salvarUsuario(user)

lerUsuarios()

    







