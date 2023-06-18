import merge

def merge_sort(my_list):
    # função recursiva
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index]) # começo:final
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

print(merge_sort([1,5,3,1,2,34]))