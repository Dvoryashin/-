import math

def binary_search(list, k):
    low = 0
    high = len(list) - 1
    while low <= high:
        medium = (high - low) // 2
        if list[medium] == k:
            return medium
        if medium > k:
            high = medium - 1
        if medium < k:
            low = medium + 1

list = [1, 3, 5, 7, 9]

print(list, '- массив')
print(binary_search(list, 2), '- результат работы функции')

