def find_pairs(arr1, arr2, target):
    my_list = []
    for i in arr1:
        for j in arr2:
            if i + j == target:
                my_set = (i, j)
                print(my_set)
                my_list.insert(0, my_set)
    return my_list




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""