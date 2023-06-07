def first_non_repeating_char(str):
    my_list = []
    duplicates = []
    for char in str:
        if char in my_list and char not in duplicates:
            index = my_list.index(char)
            duplicates.append(my_list.pop(index))
        elif char not in my_list and char in duplicates:
            pass
        elif char not in my_list and char not in duplicates:
            my_list.append(char)
    if my_list != []:
        return my_list[0]
    else:
        return None




print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""