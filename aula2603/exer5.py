#dicionario
contatos = { 
    "ana": "ana@example.com", 
    "joao": "joao@example.com", 
    "maria": "maria@example.com" 
} 

#print(contatos["ana"])
contatos["jeandro"] = "jeandro@gmail.com"
#print(contatos["jeandro"])



for chave, valor in contatos.items():
    print(chave, ":", valor)


