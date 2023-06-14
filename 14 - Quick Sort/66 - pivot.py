def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(lista, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index+1):
        if lista[i] < lista[pivot_index]:
            # não entendi muito isso
            swap_index += 1
            swap(lista, swap_index, i)
    swap(lista, swap_index, pivot_index)
    return swap_index