# Abrindo o arquivo texto.txt para escrita
arquivo = open("texto.txt", "w")

# Criando a lista de frases
texto = list()
texto.append("Esta e a primeira frase do meu arquivo.\n")
texto.append("O Python facilita muito a manipulacao de dados.\n")
texto.append("Arquivo gerado com sucesso para o trabalho pratico.")

# Escrevendo no arquivo
arquivo.writelines(texto)

# Fechando o arquivo
arquivo.close()

print("Sucesso! O arquivo 'texto.txt' foi atualizado.")