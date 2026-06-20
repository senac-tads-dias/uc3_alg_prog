produto = {
   "id": 2,
   "nome": "banana",
   "fabricante":"Frutas do Bosque",
   "valor" : 2.99,
   "qtd" : 20
}

print(produto)
print(produto["nome"])
produto["nome"] = "manga"
print(produto)

del produto["qtd"]
print(produto)

if "nome" in produto:
    print("A chave existe")
print("\n\nSomente chave")

for chave in produto.keys():
   print(chave)

print("\n\nSomente valor do dicionario")
for valor in produto.values():
   print(valor)

print("\n\nchave e valor")
for chave, valor in produto.items():
   print(chave, ":", valor)






