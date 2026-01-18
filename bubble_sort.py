# Método Bubble Sort conforme o roteiro do trabalho
def bubbleSort(array):
    # Laço para percorrer todos os elementos do array
    for i in range(len(array)):
        # Laço para comparar os elementos adjacentes
        for j in range(0, len(array) - i - 1):
            # Condição: se o elemento atual for maior que o próximo
            if array[j] > array[j+1]:
                # Realiza a troca de posições
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

# Criando um array de 15 números desordenados
meu_array = [64, 34, 25, 12, 22, 11, 90, 8, 45, 72, 1, 53, 33, 19, 40]

# Aplicando o método criado
bubbleSort(meu_array)

# Exibindo o resultado final
print("Array ordenado com Bubble Sort:")
print(meu_array)