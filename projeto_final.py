# Algoritmo de ordenacao Bubble Sort para o glossario
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compara as palavras ignorando maiusculas/minusculas
            if lista[j].lower() > lista[j + 1].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# 1. Lendo o arquivo original que esta na subpasta
with open("manipulacao_arquivos/loremipsum.txt", "r") as arquivo:
    conteudo = arquivo.read()

# 2. Limpando o texto (removendo pontos e virgulas para pegar apenas as palavras)
conteudo_limpo = conteudo.replace(".", "").replace(",", "").lower()
palavras = conteudo_limpo.split()

# 3. Aplicando a ordenacao
bubble_sort(palavras)

# 4. Salvando o glossario final em um novo arquivo na pasta raiz
with open("glossario_ordenado.txt", "w") as arquivo_final:
    for item in palavras:
        arquivo_final.write(item + "\n")

print("O glossario ordenado foi gerado em 'glossario_ordenado.txt'.")