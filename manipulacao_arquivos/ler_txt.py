# Abrindo o arquivo de texto
arquivo = open("loremipsum.txt", "r")

# Guardando o que o Python leu em uma variavel
conteudo = arquivo.read()

# Mostrando o resultado no terminal
print("--- TESTE DE LEITURA ---")
print(conteudo)

# Fechando o arquivo
arquivo.close()