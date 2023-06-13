def merge(list1, list2): 
    # func que organiza duas listas que já estão sorted
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

print(merge([1,3,7,8], [1,2,3,6]))