def merge(list1, list2): 
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    if i < len(list1):
        while i < len(list1):
            combined.append(list1[i])
            i += 1

    if j < len(list2):
        while j < len(list2):
            combined.append(list2[j])
            j += 1
    
    return combined

def merge_sort(my_list):
    # função recursiva
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index]) # começo:final
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

print(merge_sort([1,5,3,1,2,34]))