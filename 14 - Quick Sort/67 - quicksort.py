def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(lista, pivot_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, len(lista)):
        if lista[i] < lista[pivot_index]:
            # não entendi muito isso
            swap_index += 1
            swap(lista, swap_index, i)
    swap(lista, swap_index, pivot_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left)
        quick_sort_helper(my_list, pivot_index+1, right)
        quick_sort_helper(my_list, left, pivot_index-1)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

print(quick_sort([4,1,2,7,8,3]))