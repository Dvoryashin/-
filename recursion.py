from random import randint

def recursion(list):
    if len(list) == 1:
        return list[0]
    first = list.pop(0)
    return first + recursion(list)

list = []

for i in range(10):
    list.append(randint(-50, 50))

print(list)
print(recursion(list))