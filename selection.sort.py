array = [75, 22, 100, 43, 11, 89, 4, 33, 50, 61, 2, 95, 18, 56, 30]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp

print("Selection Sort:", array)