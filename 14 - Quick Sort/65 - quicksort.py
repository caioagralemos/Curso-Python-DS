import pivot

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left)
        quick_sort_helper(my_list, pivot_index+1, right)
        quick_sort_helper(my_list, left, pivot_index-1)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

print(quick_sort([4,1,2,7,8,3]))