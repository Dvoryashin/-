from random import randint

def selection_sort(list):
    new_arrray = []
    while len(list) != 0:
        max_number = list[0]
        max_index = 0
        for i in range(len(list)):
            if max_number <= list[i]:
                max_number = list[i]
                max_index = i
        print(max_number)
        list.pop(max_index)
        print(list)
        new_arrray.append(max_number)
    return new_arrray

list = []

for i in range(10):
    list.append(randint(-50, 50))

print(list)
print(selection_sort(list))
