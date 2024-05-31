def divide(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = divide(lst[0:mid])
    right = divide(lst[mid:len(lst)])
    sorted = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            sorted.append(left[0])
            left.pop(0)
        else:
            sorted.append(right[0])
            right.pop(0)
    if len(right) > 0:
        sorted += right
    else:
        sorted += left
    return sorted

random_list_of_nums = [120, 45, 68, 250, 176]  
random_list_of_nums = divide(random_list_of_nums)  
print(random_list_of_nums)