def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        #на самом деле, надо выбирать рандомный элемент чтобы избежать худшего сценария. 
        pivot = list[0]
        mid = []
        less = []
        over = []
        for el in list:
            if el < pivot:
                less.append(el)
            elif el > pivot:
                over.append(el)
            else:
                mid.append(el)
        return quicksort(less) + mid + quicksort(over)

print(quicksort([4, 5, 1, 6, 8, 3, 2]))
