def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        for j in range(i):
            if my_list[i] < my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return my_list

print(insertion_sort([1,2,3,2,3]))
