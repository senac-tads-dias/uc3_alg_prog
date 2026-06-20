path_arquivo = "pasta_arquivos/aula.txt"

def escrever(texto):
    arquivo = open(path_arquivo, "w")
    arquivo.write(texto)
    arquivo.close()

def escreverNoFinal(texto):
    arquivo = open(path_arquivo, "a")
    arquivo.write(texto+"\n")
    arquivo.close()

def leituraDoArquivoInteiro():
    arquivo = open(path_arquivo, "r")
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()

def leituraLinhaPorLinha():
    arquivo = open(path_arquivo, "r")
    for linha in arquivo:
        print("Nome:",linha)
    arquivo.close()


while True:
    dado = input("Informe um texto para salvar ou fim para sair: ")

    if dado == "fim":
        break
    else:
        escreverNoFinal(dado)
    
leituraLinhaPorLinha()




