# a. Crie um array de 15 posições com números inteiros aleatórios
numeros = [54, 12, 78, 3, 99, 45, 21, 8, 67, 32, 1, 88, 10, 5, 27]

# b. Realize a ordenação utilizando o método sort
numeros.sort()

# c. Imprima o conteúdo (crescente)
print("Números em ordem crescente:", numeros)

# d. Utilize o método sort para ordem decrescente
numeros.sort(key=None, reverse=True)

# e. Imprima o conteúdo (decrescente)
print("Números em ordem decrescente:", numeros)

# f. Crie um array de strings e repita os passos
dados = ["Eduardo", "Ana", "Zeca", "Beatriz", "Carlos"]
dados.sort()
print("\nStrings em ordem alfabética:", dados)
dados.sort(reverse=True)
print("Strings em ordem inversa:", dados)