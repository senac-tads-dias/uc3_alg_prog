alunos = []

while True:
    nome  = input("\nInforme o nome do aluno: ")

    if nome == "fim":
        break
    else:
        aluno = {}
        aluno["nome"] = nome
        nota1 = float(input("Informe a nota 1: "))
        nota2 = float(input("Informe a nota 2: "))
        aluno["nota1"] = nota1
        aluno["nota2"] = nota2
        aluno["media"] = (nota1+nota2)/2
        #print("\nAluno add: ",aluno)
        alunos.append(aluno)
nome_maior_media = ""
maior_media = 0
qtd = 0
print("Medias dos Alunos: \n")
for aluno in alunos:
    print("Aluno: ", aluno["nome"], "Média: ", aluno["media"])
    #maior media
    if maior_media < aluno["media"]:
        maior_media = aluno["media"]
        nome_maior_media = aluno["nome"]
    
    #quantidade de media menor que 6
    if aluno["media"] < 6.0:
        qtd += 1

print("\nO aluno com a maior media: ", nome_maior_media)
print("\nA quantidade de alunos com media menor que 6 é: ", qtd)

        


