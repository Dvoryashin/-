from random import randint
  
def bubble_sort(lst):
    for i in range(0, len(lst)):
        for d in range(0, len(lst) - 1 - i):
            if lst[d] > lst[d + 1]:
                temp = lst[d]
                lst[d] = lst[d + 1]
                lst[d + 1] = temp
    return lst

list = []

for i in range(10):
    list.append(randint(-50, 50))

print(list)
print(bubble_sort(list))
            